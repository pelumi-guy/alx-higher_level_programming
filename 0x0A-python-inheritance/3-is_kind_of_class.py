#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """a function that checks if object is an
    instance of a given class or an instance of
    an inherited

    Args:
        @obj: object instance
        @a_class: class to check for

    Return:
        True if the object is an instance
        of the specified class; otherwise False."""

    return isinstance(obj, a_class)
