# search.py

def simplesearch(alarms, query):
    """
    simple search for an alarm label inside a list of Alarm objects.
    Returns the index if found, otherwise None.
    """
    query = query.lower()
    for i in range(len(alarms)):
        if alarms[i].label.lower() == query:
            return i
    return None
