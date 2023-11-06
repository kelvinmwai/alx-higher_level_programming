#!/usr/bin/python3

def max_integer(my_list):
    if len(my_list) == 0:
        return (None)

    max_numb = my_list[0]
    for b in range(len(my_list)):
        if my_list[b] > max_numb:
            max_numb = my_list[b]

    return (max_numb)
