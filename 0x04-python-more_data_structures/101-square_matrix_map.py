#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    resMatx = []
    resMatx = list(map(lambda x: list(map(lambda y: y*y, x)), matrix))
    return resMatx
