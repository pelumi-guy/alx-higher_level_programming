#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        @matrix: matrix to be divided
        @div: divisor

    Return:
        new matrix containing quotients of division of
        elements of argument matrix by divisor
    """
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for elm in row:
            if not isinstance(elm, int) and not isinstance(elm, float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    ret = []
    for row in matrix:
        newRow = []
        for elm in row:
            newRow.append(round((elm / div), 2))
        ret.append(newRow)

    return ret
