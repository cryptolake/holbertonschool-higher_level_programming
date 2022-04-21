#!/bin/bash
# Post with json
curl -X POST "$1" -H 'Content-Type: application/json' -d "$(cat "$2")"
