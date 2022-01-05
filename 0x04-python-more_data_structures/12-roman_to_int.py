#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0
    while i < len(roman_string):
        now = roman_table[roman_string[i]]
        try:
            after = roman_table[roman_string[i + 1]]
        except IndexError:
            after = 0
        if after > now:
            num += after - now
            i += 2
        elif after < now:
            num += after + now
            i += 2
        else:
            num += now
            i += 1
    return num
