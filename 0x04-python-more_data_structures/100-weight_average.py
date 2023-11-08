#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg = 0
    div = 0
    for y in my_list:
        avg += y[0] * y[1]
        div += y[1]
    return float(avg / div)
