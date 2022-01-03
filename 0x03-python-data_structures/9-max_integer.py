#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    mx = float('-inf')
    for x in my_list:
        if x > mx:
            mx = x
    return mx
