from alarm import Alarm
from data_storage import Repository


class Profile:
    """Represents a user profile with its own alarms (no reminders)."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Each user has their own JSON file
        self.repo = Repository(path=f"data/{self.username}.json")

        # Load existing alarms (or empty list if file doesn't exist)
        self.alarms = self.repo.load(Alarm)

    def save(self):
        """Save current alarms to external storage."""
        self.repo.save(self.alarms)

    def add_alarm(self, alarm):
        """Add a new alarm to the profile and save."""
        self.alarms.append(alarm)
        self.save()
        print(f"Alarm '{alarm.label}' added to {self.username}.")

    def show_profile_summary(self):
        """Print a human-readable summary (for debugging / CLI use)."""
        print(f"\n--- {self.username}'s Profile Summary ---")
        print(f"Alarms ({len(self.alarms)}):")
        for alarm in self.alarms:
            print(f"  - {alarm.label} at {alarm.time}")
        print("-----------------------------------")
