#!/usr/bin/python3
"""Module to find maximum integer in a list"""

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        Return None if list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    y = 1
    while y < len(list):
        if list[y] > result:
            result = list[y]
        y += 1
    return result
