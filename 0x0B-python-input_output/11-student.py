#!/usr/bin/python3
"""11. Student to disk and reload"""
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file


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

    def reload_from_json(self, json):
        """method that replaces all attributes
        of the Student instance

        Args:
            @json: json dictionary to read from"""
        for key, value in json.items():
            setattr(self, key, value)
