#!/usr/bin/python3
"""Json api."""
from sys import argv
import requests

if __name__ == "__main__":
    if argv[1]:
        q = argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        resp = r.json()
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
        exit()

    if len(resp) == 0:
        print("No result")
    else:
        id = resp[0]['id']
        name = resp[0]['name']
        print("[{}] {}".format(id, name))
