#!/bin/bash
# Get body of request
[[ $(curl -s -I "$1" | head -1 | cut -d' ' -f2) == "200" ]] && curl -s -X "GET" "$1"
