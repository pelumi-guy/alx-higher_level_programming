#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that defines a square
    inheriting from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes instance of square"""
        if type(size) != int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrides the parent __str__ method so that
        it returns  a string with format:
        [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y}" + \
               f" - {self.size}"

    @property
    def size(self):
        """Retrieves the size attribute of the rectangle"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets attribute size of square instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates the square assigning
         an argument to each attribute

         Arg:
            @args: list of arguements
            @kwargs: list of arguments in keyword, value pairs"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method of Square class that returns
        dictionary representation of the class"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
