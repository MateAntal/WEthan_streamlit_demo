import streamlit as st
from datetime import datetime, date
import os
from engine import Engine

st.title("WEthan – Alarm Demo")

# Initialize engine once per session
if "engine" not in st.session_state:
    st.session_state.engine = Engine()

engine = st.session_state.engine

# ------------------------------
# ADD ALARM
# ------------------------------
st.header("Add Alarm")

label = st.text_input("Alarm Label")
time_input = st.time_input("Alarm Time")
repeat = st.selectbox("Repeat", ["none", "daily", "weekdays"])

uploaded_voice = st.file_uploader(
    "Upload a voice file", type=["mp3", "wav", "m4a", "aac", "ogg"]
)

if st.button("Create Alarm"):
    if not uploaded_voice:
        st.error("Please upload a voice file.")
    elif not label:
        st.error("Please enter a label for the alarm.")
    else:
        # Save uploaded file locally
        os.makedirs("voices", exist_ok=True)
        voice_path = os.path.join("voices", uploaded_voice.name)
        with open(voice_path, "wb") as f:
            f.write(uploaded_voice.getbuffer())

        alarm_time = datetime.combine(date.today(), time_input)
        engine.add_alarm(alarm_time, voice_path, repeat, label)
        st.success("Alarm created and saved!")

# ------------------------------
# VIEW CURRENT ALARMS
# ------------------------------
st.header("Current Alarms")
alarms = engine.get_alarms()

if len(alarms) == 0:
    st.info("No alarms saved yet.")
else:
    for a in alarms:
        st.write(f"**{a.label}** – {a.time} – Repeat: {a.repeat}")
