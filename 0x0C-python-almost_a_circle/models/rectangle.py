#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """class that defines a rectangle
    inheriting from Base class"""

    className = 'Rectangle'
    instances = []

    def __init__(self, width, height, x=0, y=0, id=None):
        """instatntiates rectangle class
        Arg:
            @width: width of rectangle
            @height: height of rectangle
            @x: attribute x of rectangle
            @y: attribute y of rectangle
        """
        # if not isinstance(width, int):
        #     raise TypeError('width must be an integer')
        # if width <= 0:
        #     raise ValueError('width must be > 0')
        # if not isinstance(height, int):
        #     raise TypeError('height must be an integer')
        # if height <= 0:
        #     raise ValueError('height must be > 0')
        # if not isinstance(x, int):
        #     raise TypeError('x must be an integer')
        # if x < 0:
        #     raise ValueError('x must be >= 0')
        # if not isinstance(y, int):
        #     raise TypeError('y must be an integer')
        # if y < 0:
        #     raise ValueError('y must be >= 0')
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Retrieves attribute x of rectangle instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the attribute x of rectangle instance"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Retrieves attribute y of rectangle instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the attribute x of rectangle instance"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle in stdout
        using character #"""
        for w in range(self.__y):
            print()
        for w in range(self.__height):
            for i in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """overrides the parent __str__ method so that
        it returns  a string with format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" + \
                           f" - {self.__width}/{self.__height}"


    def update(self, *args, **kwargs):
        """Updates the rectangle assigning
         an argument to each attribute

         Arg:
            @args: list of arguements
            @kwargs: list of arguments in keyword, value pairs"""
        if args and len(args) != 0:
            for a, arg in enumerate(args):
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method of Rectangle class that returns
        dictionary representation of the class"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
