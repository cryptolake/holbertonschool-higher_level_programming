#!/usr/bin/python3
"""Append to file."""


def append_write(filename="", text=""):
    """Append to file."""
    with open(filename, "a", encoding='UTF8') as f:
        chars = f.write(text)
    return chars
