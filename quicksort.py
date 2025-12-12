# quicksort.py
# Custom quicksort to order alarms by priority, then by time.

import random


def quicksort(alarms):
    """
    Sort a list of Alarm objects:
    - higher priority comes first
    - if priority is equal, earlier time comes first
    Returns a new sorted list
    """
    # Base case
    if len(alarms) < 2:
        return alarms

    def comes_before(a, b):
        # 1) Higher priority first
        if a.priority != b.priority:
            return a.priority > b.priority
        # 2) If same priority, earlier time first
        return a.time < b.time

    # Recursive case
    pivot = random.choice(alarms)
    left = []
    right = []

    for alarm in alarms:
        if alarm is pivot:
            continue
        if comes_before(alarm, pivot):
            left.append(alarm)
        else:
            right.append(alarm)

    return quicksort(left) + [pivot] + quicksort(right)
