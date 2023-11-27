#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize  Rectangle instance in constructor.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: the width, must be a +ve integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= zero")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of a rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of rectangle instance
        Args:
            value:height, must be a +ve integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= zero")
        self.__height = value
