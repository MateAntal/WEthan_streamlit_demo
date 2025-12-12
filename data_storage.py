# data_storage.py
# Handles saving and loading Alarms from a JSON file.

import os
import json
from datetime import datetime


def _serialize_alarm(a):
    """Convert an Alarm object into a JSON-friendly dictionary."""
    return {
        "time": a.time.isoformat(),
        "voice_file_path": a.voice_file_path,
        "repeat": a.repeat,
        "label": a.label,
        "active": a.active,
    }


def _deserialize_alarm(d, AlarmClass):
    """Rebuild an Alarm object from a dictionary."""
    a = AlarmClass(
        time=datetime.fromisoformat(d["time"]),
        voice_file_path=d["voice_file_path"],
        repeat=d["repeat"],
        label=d["label"],
    )
    a.active = d.get("active", True)
    return a


class Repository:
    """Manages saving and loading alarms to/from a JSON file."""

    def __init__(self, path):
        self.path = path
        # Make sure the directory for this path exists
        directory = os.path.dirname(self.path)
        if directory:
            os.makedirs(directory, exist_ok=True)

    def save(self, alarms):
        """Save the given list of Alarm objects to JSON."""
        data = {
            "alarms": [_serialize_alarm(a) for a in alarms],
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"[SAVE] {len(alarms)} alarms → {self.path}")

    def load(self, AlarmClass):
        """Load alarms from JSON. Return empty list if file is missing."""
        if not os.path.exists(self.path):
            print(f"[LOAD] No file found — starting with 0 alarms.")
            return []

        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)

        alarms = [_deserialize_alarm(d, AlarmClass) for d in data.get("alarms", [])]
        print(f"[LOAD] Loaded {len(alarms)} alarms.")
        return alarms
