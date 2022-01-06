#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    total_weight = 0
    for couple in my_list:
        score, weight = couple
        average += score * weight
        total_weight += weight
    average /= total_weight
    return average
