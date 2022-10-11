#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret_list = [0] * list_length
    i = 0
    while i < list_length:
        try:
            ret_list[i] = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            i += 1

    return ret_list
