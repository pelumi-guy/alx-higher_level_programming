#!/usr/bin/python3
"""defines a class Square instantiated with a private size variable"""


class Square:
    """a square object"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    # Getter method to retrieve private attribute __size
    @property
    def size(self):
        """retrieves the size of a square"""
        return self.__size

    # Getter method to update private attribute __size
    @size.setter
    def size(self, value):
        """updates the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
