#!/usr/bin/python3
"""13. Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        @filename: name of file to write to
        @search_string: string to find in file
        @new_string: string to insert"""
    with open(filename, 'r') as fp:
        lines = []
        for line in fp:
            lines.append(line)
            if line.find(search_string) >= 0:
                lines.append(new_string)

    with open(filename, 'w') as fp:
        fp.write(''.join(lines))
