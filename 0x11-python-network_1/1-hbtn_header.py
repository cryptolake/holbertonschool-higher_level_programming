#!/usr/bin/python3
"""Get http header."""
from sys import argv
import urllib.request


def main(argv):
    """Run main function."""
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    main(argv)
