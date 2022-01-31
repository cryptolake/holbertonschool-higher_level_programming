#!/usr/bin/python3
"""A Geometry class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A simple square is a rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
