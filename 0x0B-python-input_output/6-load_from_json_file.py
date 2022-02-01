#!/usr/bin/python3
"""json file to object."""
import json


def load_from_json_file(filename):
    """json file to object."""
    with open(filename, mode="r") as f:
        json_data = f.read()
    json_data = json.loads(json_data)
    return json_data
