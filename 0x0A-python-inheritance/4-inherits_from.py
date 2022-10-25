#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """a function that checks if object is an
    instance of a given class that inherited
    (directly or indirectly) from the specified
    class ; otherwise False.

    Args:
        @obj: object instance
        @a_class: class to check for

    Return:
        True if the object is an instance of inherited
        class of the specified class; otherwise False."""

    if a_class in type(obj).__mro__ and a_class != type(obj):
        return True
    else:
        return False
