#!/usr/bin/python3
def a_func():
    count = 0
    st = "BestSchool"

    def actualf():
        nonlocal count
        nonlocal st
        for i in range(0, count):
            st += ", BestSchool"
        count += 1
        return st
    return actualf


magic_string = a_func()
