#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters."""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    tokens = (".", "?", ":")
    for r in tokens:
        text = text.replace(r + ' ', r)

    for c in text:
        if c in tokens:
            print(c, end="\n\n")
        else:
            print(c, end="")
