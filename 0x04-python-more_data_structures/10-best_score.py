#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_dict = {'max_val': 0, 'key': ""}

    for key in a_dictionary:
        if a_dictionary[key] > max_dict['max_val']:
            max_dict['max_val'] = a_dictionary[key]
            max_dict['key'] = key

    return max_dict['key']
