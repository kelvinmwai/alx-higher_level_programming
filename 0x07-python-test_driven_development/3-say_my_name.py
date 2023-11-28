#!/usr/bin/python3
"""Definition for name-printing function"""

def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
        first_name: the 1st name to print.
        last_name: the 2nd name to print.
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
