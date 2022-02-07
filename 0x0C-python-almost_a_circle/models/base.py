#!/usr/bin/python3
"""Base Class of all classes."""
import json
from os import open, read, write


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
