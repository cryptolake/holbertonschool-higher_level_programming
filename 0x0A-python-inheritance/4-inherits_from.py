#!/usr/bin/python3

def inherits_from(obj, a_class):
    return a_class in list(obj.__class__.__mro__)[1:]
