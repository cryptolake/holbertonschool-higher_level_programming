#!/usr/bin/python3
"""Status of api."""
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    bytes = response.read()
    decoded = bytes.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(bytes))
    print("\t- content:", bytes)
    print("\t- utf8 content:", decoded)
