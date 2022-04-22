#!/usr/bin/python3
"""Json api."""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get("https://api.github.com/user",
                     auth=(argv[1], argv[2]))
    resp = r.json()
    try:
        print(resp['id'])
    except KeyError:
        print(None)
