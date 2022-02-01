#!/usr/bin/python3
import json
"""class to json."""


def class_to_json(obj):
    """class to json."""
    return json.dumps(obj.__dict__)
