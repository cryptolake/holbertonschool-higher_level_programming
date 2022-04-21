#!/bin/bash
# Get body of request
curl -Ls -I -X 'GET' "$1" | grep -q "200 OK" && curl -s -L -X "GET" "$1"
