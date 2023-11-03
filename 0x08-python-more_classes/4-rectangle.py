#!/usr/bin/python3

"""
Reactangele class
"""


class Rectangle:
    """
    Reactange class with width and height
    """

    def __init__(self, width=0, height=0):
        """
        initialize
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter function
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter function
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        calculates the area of the reactangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        calculates the parameter of reactangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2*(self.width + self.height)

    def __str__(self):
        """
        print Reactangle using #
        """
        return str(((lambda x: x * self.width + '\n')("#")
                    * self.height).strip("\n"))

    def __repr__(self):
        """
        returns string implementation of a class
        """
        return f"Rectangle({self.width}, {self.height})"
