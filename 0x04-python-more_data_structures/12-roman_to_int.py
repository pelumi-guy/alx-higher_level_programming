#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    upCased = roman_string.upper()
    sum = 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    while i < len(upCased):
        if i < len(upCased) - 1:
            if values[upCased[i]] >= values[upCased[i + 1]]:
                sum += values[upCased[i]]
                i += 1
            else:
                sum += (values[upCased[i + 1]] - values[upCased[i]])
                i += 2
        else:
            sum += values[upCased[i]]
            i += 1
    return sum
