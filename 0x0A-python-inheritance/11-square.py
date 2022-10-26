#!/usr/bin/python3
"""Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class defining a square,
    inheriting Rectangle class"""

    def __init__(self, size):
        """Initializes rectangle class.

        Args:
            size (int): The size of width and height
            of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns printable string representation
        of rectangle.

        Return:
            Square description- [Square] <width>/<height>"""
        return f"[Square] {self.__size}/{self.__size}"
