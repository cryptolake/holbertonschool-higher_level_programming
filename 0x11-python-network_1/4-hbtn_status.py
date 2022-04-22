#!/usr/bin/python3
"""Status of api."""
import requests

r = requests.get('https://intranet.hbtn.io/status')
content = r.text
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
