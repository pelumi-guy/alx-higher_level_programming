#!/usr/bin/python3
"""7. Load, add, save"""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = 'add_item.json'
    my_list = []
    try:
        my_list += load_from_json_file(filename)
    except FileNotFoundError:
        pass
    for i in range(1, len(argv)):
        my_list.append(argv[i])

    save_to_json_file(my_list, filename)
