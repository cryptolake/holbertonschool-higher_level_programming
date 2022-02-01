#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """Read file."""
    with open(filename, mode='r', encoding='UTF8') as f:
        data = f.read()
        f.close()
    print(data, end="")
