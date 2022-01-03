#!/usr/bin/python3

def main():
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
        res = add(a, b)
    elif sign == "-":
        res = sub(a, b)
    elif sign == "*":
        res = mul(a, b)
    elif sign == "/":
        res = div(a, b)
    print("{:d} {} {:d} = {:d}".format(a, sign, b, res))

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    main()
