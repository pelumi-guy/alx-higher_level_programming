#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """a rebel class that inherits int class
    and has == and != reversed"""

    def __eq__(self, __x: object) -> bool:
        """method to invert == operator

        Args:
            x: other number to compare with

        Return:
            True if not equal:
            False otherwise"""
        return super().__ne__(__x)

    def __ne__(self, __x: object) -> bool:
        """method to invert != operator

        Args:
            x: other number to compare with

        Return:
            True if equal:
            False otherwise"""
        return super().__eq__(__x)
