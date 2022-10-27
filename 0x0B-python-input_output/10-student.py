#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """a class that defines student by
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        """Ïnitiializes an instance of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that retrieves a dictionary
        representation of a Student instance"""
        if attrs:
            ret_dict = {}
            for attr in attrs:
                try:
                    ret_dict[attr] = getattr(self, attr)
                except AttributeError:
                    pass
            return ret_dict
        else:
            return self.__dict__
