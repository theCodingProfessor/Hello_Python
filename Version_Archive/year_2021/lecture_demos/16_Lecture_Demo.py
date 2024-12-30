# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# 16_Lecture_Demo.py
# CIS-135 Python
# Lecture Code Demo on Python Objects (Getters and Setters)

# Encapulate in Code

class Student:

  # Construct new student object
  def __init__(self,first_name, last_name, student_id):
    self.first_name = first_name
    self.last_name = last_name
    self.stu_id = student_id
    return

  # Get methods; method (a functions of a class) which retrieves data
  def get_last_name(self):
    return self.last_name

  def get_first_name(self):
    return self.first_name

  def get_student_id(self):
    return self.stu_id

  # Set Methods
  def set_student_id(self,new_id):
    self.stu_id = new_id
    print("The updated number is", self.stu_id)
    return

new_student = Student("Clinton","Goodman",123)
print(new_student)

# Want to see the student's first and last name
#print(new_student.last)
print(new_student.get_last_name())
print(new_student.get_first_name())
print("Old student id", new_student.get_student_id())
new_id = input("Please type in a new id number: ")
new_student.set_student_id(new_id)
print("New student id", new_student.get_student_id())