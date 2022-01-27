#!/usr/bin/python3
"""print a square."""


def print_square(size):
    """print a square."""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    rect = ""
    if size == 0:
        print("")
        return
    for i in range(0, size):
        for j in range(0, size):
            rect += '#'
        rect += "\n"
    rect = rect[0:len(rect) - 1]
    print(rect)
