# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# 14_Lecture_Demo.py
# CIS-135 Python
# Lecture 14; Introduction to Object Oriented Programming

# Describe an Class for an Object
class Person():
  def __init__(self,their_name):
    self.persons_name = their_name
    return

  def printName(self):
    return self.persons_name

myPerson = Person("Clinton")
print(myPerson.printName())
