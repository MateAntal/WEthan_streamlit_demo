# search.py

def simplesearch(tasks, item):
    """Linear search for a title inside a list of task titles."""
    item = item.lower()
    for i in range(len(tasks)):
        if tasks[i].lower() == item:
            return i
    return None
