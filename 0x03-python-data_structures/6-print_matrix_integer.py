#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) > 0:
        for row in matrix:
            for elm in row:
                print("{}".format(elm), end=' ' if row.index(elm) <
                      len(row) - 1 else '\n')
    else:
        print()
