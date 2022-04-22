#!/usr/bin/python3
"""Get http header."""
from sys import argv
import urllib.request

with urllib.request.urlopen(argv[1]) as response:
    print(response.getheader('X-Request-Id'))
