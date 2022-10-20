#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """a function that prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print('#', end='')
        if i != size - 1:
            print()


# print_square(4)
# print("--")
# try:
#     print_square(-1)
# except Exception as e:
#     print(e)
# print("--")
# try:
#     print_square(-1.3)
# except Exception as e:
#     print(e)
