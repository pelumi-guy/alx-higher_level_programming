#!/usr/bin/python3
"""5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object
    to a text file, using a JSON representation

    Args:
        @my_obj: object to write
        @filename: name of file to be written to
    """
    with open(filename, 'w') as fp:
        json.dump(my_obj, fp)
