#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for x, c in enumerate(str):
        if x != n:
            newstr += c
    return newstr
