# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# student_clinton.py
# CIS-135 Python
# Assignment #29  Object Inheritance in Python

from person_clinton import Person
import datetime

# Rubric 1 Point:
# Create a new Python Class named Student (which inherits the class
# Person) created in assignment #28. Please do NOT copy and paste
# the person.py class, but instead import the class file
# (from person_file import Person) to this script.

# Rubric 1 Point:
# New to the Student class, add two parameters; 1) A integer value
# named year_started (which automatically generates the current
# year using the Python datetime library), and; 2) A Python dictionary
# named class_list with a string-key for the name of the class and
# a string-value for the grade earned {i.e., 'Python': 'A'}.

class Student(Person):
  year = datetime.datetime.now()
  def __init__(self, first_name, last_name, favorite_food):
    super().__init__(first_name, last_name, favorite_food)
    self.year_started = self.year.strftime("%Y")
    self.class_list = {}

  # Rubric 2 Points:
  # Create a method for the Student class named student_report that
  # prints the student's name (first and last), the list of the
  # classes for the student (with grades if available), and the year
  # the student record was initially created.
  def run_report(self):
    print(f'\n\tStudent Name: \t{self.first_name.title()} {self.last_name.title()}')
    print(f'\tYear Started: \t{self.year_started}')
    print(f'\tClass List:')
    course_keys = self.class_list.keys() # {'string-key': 'string-value'}
    for course in course_keys:
      print(f'\t\t {course}: {self.class_list[course]}')
    print(f'\tEnd of report for student: {self.last_name.title()}')
    return

# Rubric 1 Point:
# Test the Student class, by creating an instance of the object, and
# give it data to populate each required field. Once you have confirmed
# that the student object is working, comment out the test data.

# fn = 'clinton'
# ln = 'garwood'
# ff = ''
# test_student = Student(fn,ln,ff)
# test_student.run_report()
