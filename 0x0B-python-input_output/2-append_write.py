#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """a function that appends a string to
    a text file (UTF8) and returns the
    number of characters written.

    Args:
        @filename: file to be read
        @text: text string to write"""

    with open(filename, 'a', encoding="utf-8") as fp:
        return fp.write(text)
