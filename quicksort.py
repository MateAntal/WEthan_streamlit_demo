# quicksort.py
# Custom quicksort to order tasks/reminders by "urgency".
# Urgency combines priority and days until due date.

import random
from datetime import date, datetime


def _priority_value(priority):
    """
    Convert priority to a numeric value.
    Supports both strings ("high", "medium", "low") and integers.
    Higher value = more important.
    """
    if isinstance(priority, (int, float)):
        return priority

    # Assume string like "high", "medium", "low"
    mapping = {
        "high": 3,
        "medium": 2,
        "low": 1
    }
    return mapping.get(str(priority).lower(), 1)  # default to lowest if unknown


def _days_until(due_date):
    """
    Return number of days from today until due_date.
    Works if due_date is a date or datetime.
    """
    today = date.today()

    if isinstance(due_date, datetime):
        due = due_date.date()
    else:
        due = due_date

    return (due - today).days


def quicksort(tasks, priority_weight=7, days_weight=1):
    """
    Sort a list of tasks/reminders by urgency using quicksort (recursive, divide & conquer).
    - priority_weight: how much importance matters
    - days_weight: how much "days until deadline" matters
    Higher urgency should come first in the list.
    """
    # Base case:
    if len(tasks) < 2:
        return tasks

    # Recursive case:

    def urgency(t):
        # Higher priority and closer due date → higher urgency score
        p_val = _priority_value(t.priority)
        days = _days_until(t.due_date)
        return priority_weight * p_val - days_weight * days

    # Cache urgency scores so we don't recompute them many times
    u_cache = {id(t): urgency(t) for t in tasks}

    def comes_before(a, b):
        ua, ub = u_cache[id(a)], u_cache[id(b)]
        if ua != ub:
            # Higher urgency first
            return ua > ub
        # Tie-breakers:
        # 1) Higher priority
        pa, pb = _priority_value(a.priority), _priority_value(b.priority)
        if pa != pb:
            return pa > pb
        # 2) Earlier due date
        return a.due_date < b.due_date

    pivot = random.choice(tasks)
    less = []
    greater = []

    for t in tasks:
        if t is pivot:
            continue
        if comes_before(t, pivot):
            less.append(t)
        else:
            greater.append(t)

    return quicksort(less, priority_weight, days_weight) + [pivot] + quicksort(greater, priority_weight, days_weight)
