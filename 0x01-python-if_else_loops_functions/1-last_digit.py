#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = abs(number) % 10
if number < 0:
    dig = -dig
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if dig > 5:
    print("greater than 5")
else if dig == 0:
    print("0")
else:
    print("less than 6 and not 0")
