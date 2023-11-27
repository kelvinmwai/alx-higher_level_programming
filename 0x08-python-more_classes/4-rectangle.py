#!/usr/bin/python3
"""Module 4-rectangle"""


class Rectangle:
    """Rectangle class ddefinition"""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle properties in a consstructor."""
        self.width = width
        self.height = height

    def __str__(self):
        """Returns informal string representation of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle_str = ''
        for x in range(self.__height):
            for y in range(self.__width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        """Return internal string representation of a Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle"""
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
        """Sets the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
