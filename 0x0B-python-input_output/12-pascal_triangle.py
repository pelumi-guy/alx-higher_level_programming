#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """a function that returns a list of lists
    of integers representing the Pascal's triangle of n

    Args:
        @n: size of pascal's triangle
    Return:
        list of integer lists representing pascal triangle"""

    if n <= 0:
        return []

    pas_tri = []
    prev_row = [1]

    for i in range(n):
        next_row = [1]
        pas_tri.append(prev_row)
        for i in range(1, len(prev_row)):
            next_row.append(prev_row[i] + prev_row[i - 1])
        next_row.append(1)
        prev_row = next_row

    return pas_tri
