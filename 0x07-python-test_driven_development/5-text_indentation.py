#!/usr/bin/python3

"""
function that prints a text with 2 new lines after
each of these characters: ., ? and :
Prototype: def text_indentation(text):
"""


def text_indentation(text):
    """
    Text indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for letter in text:
        if letter == '.' or letter == '?' or letter == ':':
            print(letter)
            print()
            flag = 1
        else:
            if letter == ' ' and flag == 1:
                continue
            print(letter, end="")
            flag = 0
