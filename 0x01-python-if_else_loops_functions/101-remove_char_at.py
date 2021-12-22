#!/usr/bin/python3

def remove_char_at(str, n):
    """Remove charatcter at index n of string."""
    s = list(str)
    if (n < 0 or n > len(str) - 1):
        return str

    for i in range(n, len(str) - 1):
        s[i] = s[i + 1]
    s[len(str) - 1] = ''

    return ''.join(s)
