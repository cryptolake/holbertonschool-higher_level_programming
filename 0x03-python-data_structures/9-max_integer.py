#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    mx = 0
    for x in my_list: 
        if x > mx:
            mx = x
    return mx
            
