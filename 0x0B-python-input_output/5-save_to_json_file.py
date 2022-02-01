#!/usr/bin/python3
"""object to json file."""
import json


def save_to_json_file(my_obj, filename):
    """object to json file."""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
