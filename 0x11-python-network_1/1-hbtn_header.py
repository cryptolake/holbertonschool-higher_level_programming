#!/usr/bin/python3
"""Get http header."""
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print(response.getheader('X-Request-Id'))
