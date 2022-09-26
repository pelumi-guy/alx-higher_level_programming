#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None

    boolList = []
    for item in my_list:
        if item % 2 == 0:
            boolList.append(True)
        else:
            boolList.append(False)
    return boolList
