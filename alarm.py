# alarm.py
# Alarm class for WEthan: stores alarm details and basic behavior.

from datetime import datetime, timedelta
import os
import webbrowser
import pathlib

ALLOWED_AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg"}


class Alarm:
    def __init__(self, time, voice_file_path, repeat, label):
        """
        Create a new Alarm.
        - time: datetime object for when the alarm should ring
        - voice_file_path: path to an audio file on disk
        - repeat: "none", "daily", or "weekdays"
        - label: short description for the alarm
        """
        self.time = time                      # when the alarm should ring
        self.voice_file_path = voice_file_path  # path to the audio file
        self.repeat = repeat                  # "none", "daily", "weekdays"
        self.label = label                    # small text to describe it
        self.active = True                    # alarm starts active

        # Validate the voice file path + extension
        self._validate_voice_file(self.voice_file_path)

    def _validate_voice_file(self, path):
        """Check that the file extension is one of the allowed audio formats."""
        _, ext = os.path.splitext(str(path))
        if ext.lower() not in ALLOWED_AUDIO_EXTS:
            raise ValueError(
                f"Voice file must be one of {sorted(ALLOWED_AUDIO_EXTS)} (got: {ext})"
            )

    def set_voice_file(self, new_path):
        """Change the voice audio file later."""
        self._validate_voice_file(new_path)
        self.voice_file_path = new_path
        print(f"[VOICE] Alarm '{self.label}' voice set to: {self.voice_file_path}")

    def play_voice(self):
        """
        Try to open the audio file with the system's default player.
        (Works on a local machine; in Streamlit deployment this may be ignored.)
        """
        uri = pathlib.Path(self.voice_file_path).resolve().as_uri()
        webbrowser.open(uri)

    def show_info(self):
        """Print a summary of the alarm (useful for debugging)."""
        print(f"Alarm: {self.label}")
        print(f" Time: {self.time}")
        print(f" Voice file: {self.voice_file_path}")
        print(f" Repeat: {self.repeat}")
        print(f" Active: {self.active}")
        print()

    def snooze(self, minutes):
        """Delay the alarm by a given number of minutes."""
        self.time = self.time + timedelta(minutes=minutes)
        print(f"Alarm '{self.label}' snoozed for {minutes} minutes.")

    def dismiss(self):
        """Turn off the alarm."""
        self.active = False
        print(f"Alarm '{self.label}' dismissed.")
