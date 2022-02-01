#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, mode='r', encoding='UTF8') as f:
        data = f.read()
        f.close()
    print(data, end="")
