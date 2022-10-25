#!/usr/bin/python3
"""Square"""
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
        Rectangle.__init__(self, size, size)
