#!/usr/bin/python3
for num in range(90):
    dig1 = num // 10
    dig2 = num % 10
    if dig1 != dig2 and dig1 < dig2 and dig1 + dig2 != 17:
        print("{}{}".format(dig1, dig2), end=', ')
print(89)
