#!/usr/bin/bash
# Get byte size of response
curl -s -v "$1" --stderr - | grep Content-Length: | cut -d' '  -f 3
