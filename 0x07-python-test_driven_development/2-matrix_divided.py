#!/usr/bin/python3

"""
function that divides all elements of a matrix.
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the
message division by zero
All elements of the matrix should be divided by div, rounded
to 2 decimal places
"""


def list_checker(matrix):
    """
    check if matrix is list and it raises exception\
    if matrix is not a list
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    list_checker(matrix)
    # check if the size of the rows are equal
    length = len(matrix[0])
    for liste in matrix:
        if len(liste) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for el in liste:
            if type(el) is not int and type(el) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    sub_list = []
    for li in matrix:
        list_checker(li)
        sub_list = []
        for el in li:
            sub_list.append(round((el / div), 2))
        new_list.append(sub_list)
    return new_list
