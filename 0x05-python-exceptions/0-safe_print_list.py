#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for elm in range(x):
            print("{}".format(my_list[elm]), end='')
            i += 1
        print()
    except IndexError:
        print()

    return i
