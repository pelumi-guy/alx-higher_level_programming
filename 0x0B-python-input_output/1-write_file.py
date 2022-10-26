#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """a function that writes a string to
    a text file (UTF8) and returns the
    number of characters written.

    Args:
        @filename: file to be read
        @text: text string to write"""

    with open(filename, 'w', encoding="utf-8") as fp:
        return fp.write(text)
