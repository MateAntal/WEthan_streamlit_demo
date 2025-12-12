from datetime import datetime
from alarm import Alarm
from profile import Profile


class Engine:
    """Thin layer between the UI (Streamlit) and the Profile/Alarms."""

    def __init__(self, username="demo_user", password="demo"):
        self.profile = Profile(username, password)

    # -------- ALARMS -------- #

    def add_alarm(self, time, voice_file_path, repeat, label):
        alarm = Alarm(
            time=time,
            voice_file_path=voice_file_path,
            repeat=repeat,
            label=label,
            priority=priority,
        )
        self.profile.add_alarm(alarm)
        return alarm

    def get_alarms(self):
        return self.profile.alarms

    def save(self):
        self.profile.save()
