#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0
    if roman_string is not str(roman_string) or roman_string is None:
        return 0

    while i < len(roman_string):
        now = roman_table[roman_string[i]]

        if i + 1 < len(roman_string):
            after = roman_table[roman_string[i + 1]]
        else:
            after = 0

        if after > now:
            num += after - now
            i += 2
        else:
            num += after + now
            i += 2
    return num
