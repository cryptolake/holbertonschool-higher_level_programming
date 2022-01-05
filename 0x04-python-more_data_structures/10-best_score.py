#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max_dict = {'max_val': float('-inf'), 'key': ""}

    for key in a_dictionary:
        if a_dictionary[key] > max_dict['max_val']:
            max_dict['max_val'] = a_dictionary[key]
            max_dict['key'] = key

    return max_dict['key']
