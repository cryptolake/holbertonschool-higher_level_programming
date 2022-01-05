#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = []
    for it1 in set_1:
        if it1 not in set_2:
            diff.append(it1)
    for it2 in set_2:
        if it2 not in set_1:
            diff.append(it2)

    return set(diff)
