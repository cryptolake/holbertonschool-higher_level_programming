#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_table = {'M': 1000, 	 'C': 100,     'X': 10,	    'I': 1,
                   'MM': 2000,	 'CC': 200,	'XX': 20,      'II': 2,
                   'MMM': 3000, 'CCC': 300, 	'XXX': 30,     'III': 3,
                   'CD': 400,     'XL': 40, 	'IV': 4,
                   'D': 500,      'L': 50, 	    'V': 5,
                   'DC': 600,     'LX': 60, 	    'VI': 6,
                   'DCC': 700,    'LXX': 70,	    'VII': 7,
                   'DCCC': 800,    'LXXX': 80,	'VIII': 8,
                   'CM': 900,     'XC': 90, 	    'IX': 9}

    num = 0
    i = 0
    if roman_string is not str(roman_string) or roman_string is None:
        return 0
    temp_str = ""
    while i < len(roman_string):
        while i < len(roman_string):
            temp_str += roman_string[i]
            if temp_str not in roman_table:
                temp_str = temp_str[:-1]
                num += roman_table[temp_str]
                temp_str = ""
                break
            i += 1
    num += roman_table[temp_str]

    return num
