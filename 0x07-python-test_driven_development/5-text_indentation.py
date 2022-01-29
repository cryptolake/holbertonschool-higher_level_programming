#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters."""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    tokens = (".", "?", ":")
    phrase = ""
    phrases = []

    for p in text:
        phrase += p
        if p in tokens:
            phrases.append(phrase)
            phrase = ""
    phrases.append(phrase)

    for p, phrase in enumerate(phrases):
        if (p == len(phrases)-1):
            print(phrase.strip(), end="")
        else:
            print(phrase.strip(), end="\n\n")
