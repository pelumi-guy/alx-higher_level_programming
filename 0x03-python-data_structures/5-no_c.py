#!/usr/bin/python3
def no_c(my_string):
    newStr = my_string.translate({ord(c): None for c in "Cc"})
    return newStr
