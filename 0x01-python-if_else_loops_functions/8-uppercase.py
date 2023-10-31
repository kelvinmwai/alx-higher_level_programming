#!/usr/bin/python3
def to_upper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (ord(c) - 32)
    else:
        return ord(c)

def uppercase(str):
    new = ""
    for c in str:
        new += "%c" % to_upper(c)
        print("{:s}".format(new))
