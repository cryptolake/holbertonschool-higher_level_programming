#!/usr/bin/python3
"""json file to object."""
import json


def load_from_json_file(filename):
    """json file to object."""
    with open(filename, mode="r") as f:
        return json.load(f)
