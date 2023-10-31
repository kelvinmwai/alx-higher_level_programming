#!/usr/bin/python3
for x in range(25, -1, -1):
    c = x + ord('A')
    if x % 2 == 1:
        c += 32
    print("{:c}".format(c), end="")
