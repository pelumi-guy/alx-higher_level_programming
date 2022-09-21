#!/usr/bin/python3
i = 0
for alph in reversed(range(ord('a'), ord('z') + 1)):
    if i % 2 == 0:
        letter = chr(alph)
    else:
        letter = chr(alph - 32)
    print("{}".format(letter), end='')
    i += 1
