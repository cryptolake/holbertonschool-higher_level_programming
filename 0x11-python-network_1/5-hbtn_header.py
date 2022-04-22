#!/usr/bin/python3
"""Status of api."""
from sys import argv
import requests

r = requests.get(argv[1])
print(r.headers["X-Request-Id"])
