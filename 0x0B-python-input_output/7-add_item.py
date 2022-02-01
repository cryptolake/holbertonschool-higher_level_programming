#!/usr/bin/python3
"""Adds all arguments to a Python list."""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """main module"""
    av = argv[1:]
    save_to_json_file(av, "add_item.json")


if __name__ == "__main__":
    main()
