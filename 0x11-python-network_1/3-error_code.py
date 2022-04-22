#!/usr/bin/python3
"""Handle http errors."""
from sys import argv
from urllib import request
from urllib.error import HTTPError


def main(argv):
    """Run main function."""
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    main(argv)
