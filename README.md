WEthan – Smart Alarm Demo
A lightweight, educational prototype demonstrating data structures, file handling, sorting algorithms, search techniques, and real-time interaction using Streamlit.

Overview
WEthan is a smart alarm demo application built as part of a data structures and algorithms project.
It showcases:
Creating, storing, and managing alarms
Sorting alarms by priority using a quicksort implementation
Searching alarms using a simple linear search
JSON-based storage
A clean, interactive Streamlit UI

Features
Create Alarms using OOP:
Attributes for alarm label, time, repeat mode, priority, and a custom audio file for the alarm sound.
We decided to store alarms in lists because
Searching is more important than inserting and deleting, so the list is better than a hash table.
Alarms are not that many, so list operations are extremely fast.
Simple to iterate through for sorting and searching.
Easy to append, delete, and reorder.
Priority-Based Sorting
Alarms are automatically sorted using a quicksort algorithm
Sorted by:
Priority (high → low)
If tie: alarm time (earliest first)
Search Alarms
Search by alarm label using a simple linear search (simple search)
Alarm Ringing
When the alarm time is reached:
A visual alert appears
The audio file plays automatically
A Stop Alarm button allows the user to stop it
Works inside GitHub Codespaces environment
Delete Alarms
Each alarm has a delete button to remove the alarm from the list.
UI refreshes immediately after deletion


Demo Instructions 
To run the app use GitHub Codespaces to ensure consistency.
Go to the GitHub repository
Click Code 

Codespaces - Create Codespace

This may take some time, refresh if the process is not executed properly. 
In the Codespace terminal, run:
streamlit run streamlit_app.py
	
The app will open in the Codespaces browser, you have to allow this
Please enjoy the demo for example you can try with this task
Create an alarm for 1–2 minutes ahead
When the time arrives:
The alarm will appear in red
Click Stop Alarm to stop it


Project Structure
.
├── alarm.py              # Alarm class with validation, snooze, dismiss, etc.
├── engine.py             # Connects UI with Profile & Alarms
├── data_storage.py       # Loads and saves alarms in JSON
├── profile.py            # Holds user alarms
├── quicksort.py          # Custom quicksort for priority sorting
├── search.py             # Simple linear search for alarm labels
├── streamlit_app.py      # Main Streamlit UI
├── voices/               # Uploaded audio files
└── data/
    └── demo_user.json    # Stored alarms



Technologies Used
Python (backend)
Streamlit (UI frontend)
JSON (data storage)
Algorithm implementations:
Quicksort (for organizing based on both priority and due date)
Simple search (small quantities of alarms makes it efficient, also couldn’t use binary since the list is not alphabetically sorted)
Datetime module (important for due dates)
Browser-based audio playback

Limitations
Alarm ringing doesn’t work
This is a demo prototype showing algorithms and datastructures, not an actual alarm system

Acknowledgements
Streamlit documentation
freeCodeCamp: How to Write a Good README
Professor Antonio López Rosell (IE University)
Team members: David Hyeon, Maximiliano Biatturi, Máté Antal, Theodor David Ethan Jessup, Bartolome Urda


