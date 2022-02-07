#!/bin/python3
from models.base import Base
import json
"""A rectangle class."""


class Rectangle(Base):
    """
        A rectangle class.
        ...

        Attributes:
        -----------

        width : int
            width of rectangle
        height : int
            height of the rectangle
        x : int
            position of rectangle in the x axis
        y : int
            position of rectangle in the y axis
        id : int
            id of rectangle

        Methods
        -------
        area()
            return area of rectangle
        display()
            display the rectangle
        update()
            update values of class instance

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def display(self):
        for y in range(0, self.y):
            print()
        for h in range(0, self.height):
            for x in range(0, self.x):
                print(' ', end="")
            for w in range(0, self.width):
                print('#', end="")
            print()

    @staticmethod
    def type_check(name, obj):
        if type(obj) is not int:
            raise TypeError("{:s} must be an integer".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.type_check("width", w)
        if (w <= 0):
            raise ValueError("width must > 0")
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        self.type_check("height", h)
        if (h <= 0):
            raise ValueError("height must > 0")
        self.__height = h

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.type_check("x", x)
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.type_check("y", y)
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.width * self.height

    def update(self, *args, **kwargs):
        updates = ["id", "width",
                   "height", "x", "y"]
        if (args):
            for i in range(0, len(args)):
                setattr(self, updates[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
