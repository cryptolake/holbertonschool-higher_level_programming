#!/usr/bin/python3

case = 0
for i in range(ord('z'), ord('a') - 1, -1):
    str = "{:c}".format(i)
    if (case):
        print(str.upper(), end="")
        case = 0
    else:
        print(str, end="")
        case = 1
