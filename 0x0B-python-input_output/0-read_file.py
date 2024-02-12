#!/usr/bin/python3

 """
 this module ....
 reades the content of the file
 """

 def read_file(filename=""):
     """
     reades the content of the file
     """
     with open("filename", "r","utf-8") as file:
         print(file.read())

