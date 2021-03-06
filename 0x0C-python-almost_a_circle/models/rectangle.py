#!/usr/bin/python3
"""A rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Represent instance."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """Display rectangle."""
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    @staticmethod
    def type_check(name, obj):
        """Check type with name."""
        if type(obj) is not int:
            raise TypeError("{:s} must be an integer".format(name))

    @property
    def width(self):
        """Width property."""
        return self.__width

    @width.setter
    def width(self, w):
        """Width setter."""
        self.type_check("width", w)
        if (w <= 0):
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """Height property."""
        return self.__height

    @height.setter
    def height(self, h):
        """Height setter."""
        self.type_check("height", h)
        if (h <= 0):
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """X axis property."""
        return self.__x

    @x.setter
    def x(self, x):
        """X setter."""
        self.type_check("x", x)
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Y axis property."""
        return self.__y

    @y.setter
    def y(self, y):
        """Y setter."""
        self.type_check("y", y)
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area of rectangle."""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """Update instance."""
        updates = ["id", "width",
                   "height", "x", "y"]
        if (args):
            for i in range(0, len(args)):
                setattr(self, updates[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Class to dict."""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
