#!/usr/bin/python3
"""Base Class of all classes."""
import json
import os
import turtle


class Base:
    """Base Class of all classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance."""
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turn Dictionary to json."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(my_str):
        """Json to obj."""
        if my_str is None or my_str == "":
            return []
        return json.loads(my_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """Serialise class into json file."""
        objs = []
        with open(cls.__name__ + ".json", 'w') as f:
            if list_objs is None or list_objs == []:
                json.dump(objs, f)
            else:
                for obj in list_objs:
                    objs.append(obj.to_dictionary())
                f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Create instance from dictionary."""
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            ins = cls(1, 0, 0)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """desialise json file to objects"""
        instances = []
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                objs = cls.from_json_string(f.read())
                for obj in objs:
                    instances.append(cls.create(**obj))
        return instances

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """Draw using turtle."""
        s = turtle.getscreen()
        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(0, 2):
                t.forward(rect.height)
                t.left(90)
                t.forward(rect.width)
                t.left(90)

        for sqr in list_squares:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(0, 4):
                t.forward(sqr.size)
                t.left(90)
