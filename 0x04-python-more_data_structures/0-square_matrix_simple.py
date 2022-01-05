#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nm = matrix.copy()
    for i, l in enumerate(nm):
        nm[i] = list(map(lambda x: x*x, l))
    return nm
