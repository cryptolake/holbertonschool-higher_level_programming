#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    sum_list = []
    res = 0
    n1 = 0
    n2 = 0
    for i in range(0, list_length):
        try:
            n1 = my_list_1[i]
            n2 = my_list_2[i]
        except IndexError:
            sum_list.append(0)
            print("out of range")
            return sum_list
        try:
            res = n1 / n2
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        finally:
            sum_list.append(res)
    return sum_list
