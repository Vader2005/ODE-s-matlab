import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title and inputs
st.title("Peak BAC Simulator")
st.markdown("Simulates your BAC over time after drinking 🍷🍻")

# User inputs
alcohol_vol = st.number_input("Alcohol volume consumed (litres)", value=0.03, step=0.01)
ABV = st.number_input("Alcohol by Volume (ABV%)", value=60, step=1)
body_weight = st.number_input("Your body weight (kg)", value=65, step=1)
time_minutes = st.slider("Simulation time (mins)", 30, 300, 120)

# Constants
k_1 = 0.111946
k_2 = 0.0186294
A_o = alcohol_vol * ABV * 1000

# Time range
t = np.arange(0, time_minutes + 1)

# BAC calculation
constants = (k_1 * A_o) / (k_2 - k_1)
equation = (-constants * np.exp(-k_2 * t)) + (constants * np.exp(-k_1 * t))
body_water = body_weight * 0.68
BAC = equation / (1000 * body_water)

# Plot
fig, ax = plt.subplots()
ax.plot(t, BAC)
ax.set_xlabel("Time (mins)")
ax.set_ylabel("BAC (%)")
ax.set_title("BAC % over Time")
st.pyplot(fig)

# Peak BAC
peak_BAC = np.max(BAC)
peak_time = t[np.argmax(BAC)]
st.markdown(f"### 🧠 Peak BAC: **{peak_BAC:.3f}%** at **{peak_time} minutes**")
