#!/usr/bin/python3
for alph in range(ord('a'), ord('z') + 1):
    if alph != ord('q') and alph != ord('e'):
        print('{:c}'.format(alph), end='')
