#!/bin/bash
# Show allowed methods
curl -s -I -X"TEST" "$1" | grep "Allow:" | cut -d':' -f 2 | awk '{$1=$1};1'
