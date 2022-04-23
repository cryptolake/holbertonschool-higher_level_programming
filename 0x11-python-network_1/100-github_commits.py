#!/usr/bin/python3
"""Json api."""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits?per_page=10"
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits:
        print("{}: {}".format(commit['commit']['author']['name'],
                              commit['commit']['tree']['sha']))
