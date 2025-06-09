def calculate_punctuality_score(arrival, scheduled):
    delta = (arrival - scheduled).total_seconds() / 60
    if delta < -5:
        return ("early", +1)
    elif -5 <= delta <= 5:
        return ("on_time", +1)
    elif 5 < delta <= 30:
        return ("late", -1)
    else:
        return ("missed", -1)
