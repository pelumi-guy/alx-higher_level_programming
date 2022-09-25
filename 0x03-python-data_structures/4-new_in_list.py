#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newList = my_list.copy()
    if idx < 0:
        return newList
    elif idx >= len(my_list):
        return newList

    newList[idx] = element
    return newList
