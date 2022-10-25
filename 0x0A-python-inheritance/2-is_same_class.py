#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """a function that checks if object is exact
    instance of a given class

    Args:
        @obj: object instance
        @a_class: class to check for

    Return:
        True if the object is exactly an instance
        of the specified class; otherwise False."""

    return type(obj) is a_class
