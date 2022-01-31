#!/usr/bin/python3
"""A Geometry class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A simple square is a rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
