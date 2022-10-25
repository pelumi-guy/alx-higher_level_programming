#!/usr/bin/python3
"""0. Lookup"""


def lookup(obj):
    """a function that returns the list of
    available attributes and methods of an object

    Args:
        @obj: Object to lookup

    Return:
        List containing available methods and attributes in object
    """
    return dir(obj)
