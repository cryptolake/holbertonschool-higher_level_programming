#!/usr/bin/python3
"""divide two matrices."""


def check_type(num):
    """check type of elements"""

    return type(num) is int or type(num) is float


def matrix_divided(matrix, div):
    """divide two matrices."""

    if not (check_type(div)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_len = len(matrix[0])
    new_matrix = []
    for x in matrix:
        if len(x) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(x, list):
            raise TypeError(("matrix must be a matrix (list of lists)"
                            "of integers/floats"))

        if not all(check_type(y) for y in x):
            raise TypeError(("matrix must be a matrix (list of lists)"
                            "of integers/floats"))

        new_list = [round(elem / div, 2) for elem in x]
        new_matrix.append(new_list)

    return new_matrix
