#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    argv.pop(0)
    sum = 0

    for arg in argv:
        sum += int(arg)

    print(sum)


if __name__ == "__main__":
    main()
