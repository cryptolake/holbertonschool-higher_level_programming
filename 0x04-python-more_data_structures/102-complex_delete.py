#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_bucket = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delete_bucket.append(key)
    for key in delete_bucket:
        del a_dictionary[key]
    return a_dictionary
