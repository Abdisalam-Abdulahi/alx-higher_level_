#!/usr/bin/python3

"""
writes to a file
"""


def write_file(filename="", text=""):
    """
    function that writes to a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
