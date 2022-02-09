#!/usr/bin/python3
"""Base Class of all classes."""
import json


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
