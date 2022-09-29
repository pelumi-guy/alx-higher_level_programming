#!/usr/bin/python3
def uniq_add(my_list=[]):
    past = []
    sum = 0
    for item in my_list:
        if item in past:
            continue
        else:
            sum += item
        past.append(item)
    return sum
