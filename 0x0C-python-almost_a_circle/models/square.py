#!/usr/bin/python3
from inspect import Attribute
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, s):
        self.width = s
        self.height = s

    def update(self, *args, **kwargs):
        updates = ["id", "size", "x", "y"]
        if (args):
            for i in range(0, len(args)):
                setattr(self, updates[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
