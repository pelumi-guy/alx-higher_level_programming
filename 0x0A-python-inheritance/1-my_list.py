#!/usr/bin/python3
"""My list"""


class MyList(list):
    """"MYList that inherits list with method
    to print sort list
    """
    def print_sorted(self):
        """Public instance method to print list in
        sorted ascending order"""
        print(sorted(self))
