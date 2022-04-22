#!/usr/bin/python3
"""Get http header."""
from sys import argv
from urllib import request

with request.urlopen(argv[1]) as response:
    print(response.getheader('X-Request-Id'))
