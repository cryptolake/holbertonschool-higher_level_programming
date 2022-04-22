#!/usr/bin/python3
"""Send a POST request."""
from sys import argv
from urllib import request, parse


def main(argv):
    """Run main function."""
    data = {'email': argv[2]}
    data = parse.urlencode(data).encode()
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    main(argv)
