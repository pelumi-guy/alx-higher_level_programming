#!/usr/bin/python3
i = 0
for alph in reversed(range(ord('a'), ord('z') + 1)):
    if i % 2 == 0:
        print(chr(alph), end='')
    else:
        print(chr(alph - 32), end='')
    i += 1
