#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds peak in a list of unsorted integers
    """
    if len(list_of_integers) == 0:
        return None

    list_set = set(list_of_integers)
    return max(list_set)
