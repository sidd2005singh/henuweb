import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎧 ML Earbuds Project", layout="wide")
st.title("🎧 Enhancing Wireless Earbuds with Human-Centric Intelligence")

st.markdown(
    """
    **📎 Live App Link:**  
    👉 [Click here to open the live Streamlit app](https://o9gryqvmmqyejwtfj6ezd5.streamlit.app/)
    """,
    unsafe_allow_html=True
)


st.markdown("""
## 📜 Project Overview
This project improves **wireless earbud functionality** by leveraging **machine learning**
to enhance audio quality and contextual awareness based on user behavior, environment,
and cognitive patterns.

The system **adapts in real-time** to provide a **personalized, seamless audio experience**.
""")

st.markdown("""
## ❗ Problem Statement
Current wireless earbuds have limitations in:
- Adapting to dynamic environments (e.g., noisy streets vs. quiet offices)
- Personalizing audio profiles based on user preferences and habits
- Predicting user needs (automatic translation, focus mode, etc.)
- Optimizing audio settings (adaptive noise cancellation, EQ adjustments)
""")

st.markdown("""
## 💡 Key Features
1. **Environmental Awareness** – Detects loud traffic and boosts ANC automatically.
2. **Adaptive Sound Profiles** – Switches modes depending on GPS/Wi‑Fi location.
3. **Usage-based Prediction** – Adjusts profile based on apps like Spotify, Zoom.
4. **Personalization** – Learns from manual EQ/volume changes.
5. **Biometric Integration** – Adapts to user stress levels by altering soundscape.
""")

# Data Table from the DOCX
data = [
    ["Environmental Noise", "Built-in microphones", "ANC optimization"],
    ["User Location", "GPS/Wi-Fi/Bluetooth beacons", "Sound profile switching"],
    ["App Usage", "Connected smartphone apps (Spotify, Zoom)", "Predict audio mode"],
    ["Manual Adjustments", "User volume/EQ changes", "Personalization"],
    ["Biometric Data", "Heart rate/skin sensors (optional)", "Stress-based audio adjustments"]
]
df = pd.DataFrame(data, columns=["Data Type", "Source", "Usage"])
st.subheader("📊 Data Sources and Usage")
st.dataframe(df, use_container_width=True)

st.markdown("""
## 🤖 Proposed Machine Learning Solutions
### 1. Noise Classification Model (CNN/RNN)
- **Input:** Raw audio from microphones
- Classifies noise types (traffic, office chatter, wind)
- Activates appropriate ANC profile

### 2. Reinforcement Learning for Personalization
- **Agent:** Learns optimal audio settings
- **Reward Function:** Reduce manual adjustments over time
- Learns preferred EQ, ANC, volume in different contexts

### 3. Time-Series Forecasting (LSTM)
- Predicts future environment & user needs
- Pre-loads best audio profile in advance
""")

st.markdown("""
---
✅ **Client Value:** This solution increases user satisfaction, reduces cognitive load, and enhances safety (e.g., situational awareness in traffic) while giving a cutting-edge tech edge to earbud products.
""")
