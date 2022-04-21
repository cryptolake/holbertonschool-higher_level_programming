#!/bin/bash
# Request methods for Post
curl -X "POST" -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
