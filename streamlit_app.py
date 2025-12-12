import streamlit as st
from datetime import datetime, date
import os
from engine import Engine

st.title("WEthan – Alarm Demo")

# Initialize engine once per session
if "engine" not in st.session_state:
    st.session_state.engine = Engine()

engine = st.session_state.engine

alarm_audio_placeholder = st.empty()


# ------------------------------
# ADD ALARM
# ------------------------------
st.header("Current Alarms")
alarms = engine.get_alarms()

# Placeholder for audio playback
alarm_audio_placeholder = st.empty()

from datetime import datetime
now = datetime.now()

# Flag to detect if something is ringing
ringing_alarm = None

for a in alarms:
    if a.active and now >= a.time:
        ringing_alarm = a
        break  # only ring the first eligible alarm

# If an alarm is ringing, handle it
if ringing_alarm:
    a = ringing_alarm

    st.error(f"⏰ Alarm ringing: {a.label}!")

    # Play the alarm sound
    alarm_audio_placeholder.markdown(
        f"""
        <audio autoplay>
            <source src="{a.voice_file_path}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )

    # STOP ALARM BUTTON
    if st.button("Stop Alarm"):
        a.active = False
        engine.save()
        st.success("Alarm stopped.")
        st.experimental_rerun()  # refresh UI immediately


# ------------------------------
# VIEW CURRENT ALARMS
# ------------------------------
st.header("Current Alarms")
alarms = engine.get_alarms()

# Placeholder for audio playback
alarm_audio_placeholder = st.empty()

# Check if any alarm should ring
from datetime import datetime
now = datetime.now()

for a in alarms:
    if a.active and now >= a.time:
        st.error(f"⏰ Alarm ringing: {a.label}!")

        # Play the alarm sound automatically
        alarm_audio_placeholder.markdown(
            f"""
            <audio autoplay>
                <source src="{a.voice_file_path}" type="audio/mpeg">
            </audio>
            """,
            unsafe_allow_html=True
        )

        # Disable after ringing so it does not ring again
        a.active = False
        engine.save()

# After ringing logic display alarms
if len(alarms) == 0:
    st.info("No alarms saved yet.")
else:
    for a in alarms:
        st.write(
            f"**{a.label}** – {a.time} – Repeat: {a.repeat} – Priority: {a.priority}"
        )


# ------------------------------
# SEARCH ALARMS
# ------------------------------
st.header("Search Alarms")

search_query = st.text_input("Search by label")

if st.button("Search"):
    from search import simplesearch

    alarms_sorted = engine.get_alarms()  # already sorted list
    index = simplesearch(alarms_sorted, search_query)

    if index is None:
        st.warning("No alarm found with that label.")
    else:
        a = alarms_sorted[index]
        st.success(f"Found alarm: **{a.label}**")
        st.write(f"Time: {a.time}")
        st.write(f"Repeat: {a.repeat}")
        st.write(f"Priority: {a.priority}")
