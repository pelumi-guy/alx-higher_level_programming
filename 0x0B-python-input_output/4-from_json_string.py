#!/usr/bin/python3
"""4. From JSON string to Object"""
import json


def from_json_string(my_str):
    """a function that returns an object
    (Python data structure) represented
    by a JSON string

    Args:
        @my_str: JSON string to parse

    Return:
        Python object represented
        by JSON string"""

    return json.loads(my_str)
