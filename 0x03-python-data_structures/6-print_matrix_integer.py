#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i, y in enumerate(x):
            if i != 0:
                print(" {:d}".format(y), end="")
            else:
                print("{:d}".format(y), end="")
        print()
