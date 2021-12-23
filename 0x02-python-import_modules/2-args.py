#!/usr/bin/python3
"""Count the number of arguments and display them."""
import sys


def main():
    """Count the number of arguments and display them."""
    argv = sys.argv
    argv.pop(0)
    argc = len(argv)

    if (argc > 1):
        print("{:d} arguments:".format(argc))
    elif (argc == 1):
        print("1 argument:")
    else:
        print("0 arguments.")

    for (i, a) in zip(range(1, argc + 1), argv):
        print("{:d}: {}".format(i, a))


if __name__ == "__main__":
    main()
