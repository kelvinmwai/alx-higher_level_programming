#!/usr/bin/python3
"""Definition of  a function's attributes."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add new attribute")
    setattr(obj, att, value)
