#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for i, x in enumerate(tuple_a):
        if i > 1:
            break
        a[i] = x

    for i, y in enumerate(tuple_b):
        if i > 1:
            break
        b[i] = y
    return (a[0] + b[0], a[1] + b[1])
