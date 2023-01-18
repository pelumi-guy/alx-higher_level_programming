#!/usr/bin/python3

def rec_find_peak(list_of_integers, n, left, right):
     
    if n == 0:
        return None

    mid = left + (right - left) // 2

    #if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid])
    #       and (mid == n - 1 or list_of_integers[mid + 1] <= list_of_integers[mid])):
        
    if (mid < n - 1 and list_of_integers[mid + 1] > list_of_integers[mid]):
        return rec_find_peak(list_of_integers, n, mid + 1, right)

    elif (mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]):
        return rec_find_peak(list_of_integers, n, left, mid - 1)
    
    else:
        return (list_of_integers[mid])


def find_peak(list_of_integers):
    n = len(list_of_integers)
    return rec_find_peak(list_of_integers, n, 0, n - 1)
