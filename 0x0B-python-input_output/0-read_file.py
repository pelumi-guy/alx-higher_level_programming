#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """a function that reads a text
    file (UTF8) and prints it to stdout

    Args:
        @filename: file to be read"""

    with open(filename, 'r', encoding="utf-8") as fp:
        data = fp.read()
        print(data)
