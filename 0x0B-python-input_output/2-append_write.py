#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, "a", encoding='UTF8') as f:
        chars = f.write(text)
        f.close()
    return chars
