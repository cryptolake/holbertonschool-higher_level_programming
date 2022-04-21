#!/bin/bash
# Show allowed methods
curl -sI -X 'OPTIONS' "$1" | grep "Allow: " | sed 's/Allow: //g'
