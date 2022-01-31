#!/usr/bin/python3
"""Inheretence from builtin."""


class MyList(list):
    """Inheretence from builtin."""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
