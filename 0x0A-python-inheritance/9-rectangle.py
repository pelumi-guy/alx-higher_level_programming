#!/usr/bin/python3
"""Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class defining a rectangle,
    inheriting BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """computes area of rectangle

        Return:
            area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns printable string representation
        of rectangle

        Return:
            Rectangle description- [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width}/{self.__height}"
