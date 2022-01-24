#!/usr/bin/python3
"""A simple rectangle."""


class Rectangle:
    """Just a Simple rectangle class."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width

    def __str__(self):
        rect = ""
        if self.height == 0 or self.width == 0:
            return rect
        for i in range(0, self.height):
            for j in range(0, self.width):
                rect += "#"
            rect += "\n"
        return rect[0:len(rect) - 1]

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(arg):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            pr = 0
        else:
            pr = (self.height + self.width) * 2
        return pr
