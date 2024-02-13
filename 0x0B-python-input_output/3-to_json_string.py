#!/usr/bin/python3

"""
converts object to json string
"""
import json


def to_json_string(my_obj):
    """
    function that returns JSON representation of an object
    """
    return json.dumps(my_obj)
