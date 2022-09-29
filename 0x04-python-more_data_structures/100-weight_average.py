#!/usr/bin/python3
from functools import reduce


def weight_average(my_list=[]):
    numerator = reduce(lambda a, b: a + b,
                       list(map(lambda x: reduce(lambda a, b: a * b, x),
                            my_list)))
    denominator = reduce(lambda a, b: a + b,
                         list(map(lambda x: x[1], my_list)))
    return numerator / denominator
