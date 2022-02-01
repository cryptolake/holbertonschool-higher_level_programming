#!/usr/bin/python3
"""Student to json."""


class Student():
    """Simple student class with json support."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        cls_dict = {}
        if type(attrs) is not list:
            return self.__dict__
        for att in attrs:
            if type(att) is not str:
                return self.__dict__
            if att in self.__dict__.keys():
                cls_dict.update({att: self.__dict__.get(att)})
        return cls_dict
