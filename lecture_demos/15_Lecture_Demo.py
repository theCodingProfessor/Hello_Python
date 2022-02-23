# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# 15_Lecture_Demo.py
# CIS-135 Python
# Lecture Code Demo on Python Objects

class Person:
  # constructor is a method of the class (function)
  def __init__(self, fname, lname, mode="author"):
    self.first_name = fname
    self.last_name = lname
    self.access_level = mode
    return

  # getter for the first name
  def get_first_name(self):
    return self.first_name

  # getter for the last name
  def get_last_name(self):
    return self.last_name

  # getter for the access level
  def get_access_level(self):
    return self.access_level

  def set_access_level(self,new_level):
    self.access_level = new_level
    return

  def reveal_user(self):
    print("This user's data is {} {}, {}".format(self.first_name,self.last_name,self.access_level))
    return

f, l = "clinton", 'garwood'
new_user = Person(f, l,'editor')
print(new_user.get_first_name())
print(new_user.get_last_name())
print(new_user.get_access_level())
new_user.reveal_user()
new_user.set_access_level("admin")
new_user.reveal_user()