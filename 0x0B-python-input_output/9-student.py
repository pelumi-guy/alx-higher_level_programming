#!/usr/bin/python3
"""9. Student to JSON"""


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

    def to_json(self):
        """function that retrieves a dictionary
        representation of a Student instance"""
        return self.__dict__
