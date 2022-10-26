#!/usr/bin/python3
"""6. Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """a function that creates
    an Object from a “JSON file

    Args:
        @filename: name of file to read from

    Return:
        python object parsed from JSON string
    """

    with open(filename, 'r') as fp:
        return json.loads(fp.read())
