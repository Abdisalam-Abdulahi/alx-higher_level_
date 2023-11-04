#!/usr/bin/python3
'''
create simple Reactangle
'''


class Rectangle:
    '''
    define a reactangle
    '''
    print_symbol = '#'
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
            return (str((lambda x: x * self.__width + "\n")
                        (str(self.print_symbol)) * self.__height).strip("\n"))

    def __repr__(self):
        ''' print reactangle '''
        return ("Rectangle(" + str(self.__width) + ", "
                + str(self.__height) + ")")

    def __del__(self):
        ''' detect deletion '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the reactangle with the biggest area '''
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        if rect_1.area() < rect_2.area():
            return rect_2
