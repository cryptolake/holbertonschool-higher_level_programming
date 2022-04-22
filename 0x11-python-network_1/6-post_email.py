#!/usr/bin/python3
"""Status of api."""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
