#!/usr/bin/python3
'''
create simple Reactangle
'''


class Rectangle:
    '''
    define a reactangle
    '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        ''' returns width of the reactangel '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' set width to value '''
        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' returns heigtht of the reactangel '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' set height to value '''
        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        ''' return the area of the reactangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' return the perimeter of the reactangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        ''' print reactangle '''
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (str((lambda x: x * self.__width + "\n")("#")
                        * self.__height).strip("\n"))

    def __repr__(self):
        ''' print reactangle '''
        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __del__(self):
        ''' detect deletion '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
