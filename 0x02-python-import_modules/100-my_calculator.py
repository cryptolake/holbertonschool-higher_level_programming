#!/usr/bin/python3

import calculator_1
import sys

if __name__ == "__main__":
    argv = sys.argv
    argv.pop(0)
    argc = len(argv)
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if not argv[1] in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[0])
    b = int(argv[2])
    res = 0
    sign = argv[1]

    if sign == "+":
        res = calculator_1.add(a, b)
    elif sign == "-":
        res = calculator_1.sub(a, b)
    elif sign == "*":
        res = calculator_1.mul(a, b)
    elif sign == "/":
        res = calculator_1.div(a, b)

    print("{:d} {} {:d} = {:d}".format(a, sign, b, res))
