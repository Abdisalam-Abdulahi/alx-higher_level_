#!/usr/bin/python3

 """
 reades the content of the file
 """

 def read_file(filename=""):
     with open("filename", "r","utf-8") as file:
         print(file.read())

