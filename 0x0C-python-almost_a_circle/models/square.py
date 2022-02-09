#!/usr/bin/python3
"""A simple square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A simple square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square to str."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property
    def size(self):
        """Size property."""
        return self.width

    @size.setter
    def size(self, s):
        self.width = s
        self.height = s

    def update(self, *args, **kwargs):
        """Update class."""
        updates = ["id", "size", "x", "y"]
        if (args):
            for i in range(0, len(args)):
                setattr(self, updates[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Class to dictionary."""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
