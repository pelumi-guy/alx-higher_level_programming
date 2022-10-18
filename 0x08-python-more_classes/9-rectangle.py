#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """a class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ïnitializes rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieves the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns string to be printed"""
        if self.__width == 0 or self.__height == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret = ret + "{}".format(self.print_symbol)
            if i != self.__height - 1:
                ret = ret + '\n'
        return ret

    def __repr__(self):
        """returns official representation of string"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Handles rectangle delete"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to compare and return
        which is bigger of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle with width and height equal to size.
        Args:
            @size: The width and height of the new Rectangle.
        """
        return cls(size, size)
