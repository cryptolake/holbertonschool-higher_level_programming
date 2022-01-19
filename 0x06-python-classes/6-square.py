#!/usr/bin/python3
"""a square with attributes, methods and very safe."""


class Square():
    """Square with it's size and area."""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple)\
                or len(position) != 2 or not isinstance(position[0], int)\
                or not isinstance(position[1], int)\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple)\
                or len(position) != 2 or not isinstance(position[0], int)\
                or not isinstance(position[1], int)\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size**2

    def my_print(self):
        if (self.__size != 0):
            for p1 in range(0, self.__position[1]):
                print()
            for x in range(0, self.__size):
                for p2 in range(0, self.__position[0]):
                    print(" ", end="")
                for y in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
