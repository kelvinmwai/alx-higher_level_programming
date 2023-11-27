#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of a Rectangle instance
        Args:value:the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of a Rectangle instance
        Returns:Area of the the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of a Rectangle instance
        Returns:Perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
