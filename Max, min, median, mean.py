from statistics import median, mean


def list_mix(lst):
    return [round(f(lst), 2) for f in (max, min, median, mean)]
