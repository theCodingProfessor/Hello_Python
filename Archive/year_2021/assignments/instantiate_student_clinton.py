# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# instantiate_student_clinton.py
# CIS-135 Python
# Assignment #30 Managing Object Collections in Python

from student_clinton import Student

# Create a new Python file named instantiate_student.py which imports
# the needed Python class files Student and Person Create and demonstrates
# the basic elements of a handling a collection of Python objects in a
# menu-driven program.

# Rubric 1 Point:
# Create a function named addStudent, which prompts the user for the
# data needed (this will need to prompt the user for required 'person'
# and 'student' data) and saves the new object into an object list named
# student_records.

student_records = []

def addStudent():
  print("\n\tAdd a New Student")
  first = input("\t\tPlease enter the person's first name: ")
  last = input("\t\tPlease enter the person's last name: ")
  food = ""
  new_student = Student(first, last, food)
  student_records.append(new_student)
  print(f'\n\tNew Student Record Added.')
  print(f'\t\tStudent Name: {new_student.first_name} {new_student.last_name}')
  print(f'\t\tStudent Created: {new_student.year_started}')
  return

# Rubric 2 Points:
# Create a function named updateStudent which will allow for
# 1) Classes to be added to a Student saved in the student_records list, and
# 2) Grades to be added to classes which are saved for each student in the list.
def updateStudent():
  print("\n\tUpdate Student Menu")
  student_to_update = input("\t\tPlease enter the student last name: ")
  print(f'\t\tReceived Lastname : {student_to_update}')
  print("\n\t\t1) Add a Class to Student Record")
  print("\t\t2) Record a Grade")
  update_request = int(input("\t\t\tPlease select option 1 or 2: "))
  if update_request == 1:
    print("\t\tAdd a Class to a Student's Record")
    print(f'\t\tStudent Name: {student_to_update.title()} Class List')
    for each in student_records:
      if student_to_update == each.last_name:
        for item in each.class_list:
          print(f'\t\t\t {item}')
        this_class = input("\t\tWhat is the name of the class to add? ")
        if this_class not in each.class_list:
          each.class_list.update({str(this_class): "No Grade Reported"})
        print(f'\t\t{this_class} Added')
        each.run_report()
  elif update_request == 2:
    print(f'\t\tStudent Name: {student_to_update} Class List')
    for each in student_records:
      if student_to_update == each.last_name:
        for item in each.class_list:
          print(item)
        this_class = input("\t\tWhat class will the grade be reported for? ")
        this_grade = input("\t\tWhat is the student's grade? ")
        if this_class in each.class_list.keys():
          each.class_list[this_class] = this_grade
        print("\t\tGrade Update Complete")
        each.run_report()
  return

# Rubric 1 Point:
# Create a function named runReport which will allow an individual
# student's profile to be selected and displayed, or allow a report
# to be run which displays all the students in the Student object list.
def runReport():
  print("\n\tStudent Reports Menu")
  record_loop = 0
  while record_loop != 3:
    print("\n\t\t1) Print Individual Student Record (requires last name)")
    print("\t\t2) All Student Records (displays last name and start date)")
    print("\t\t3) Exit Reports Menu\n")
    record_loop = int(input("\t\tPlease select an option: "))
    if record_loop == 1:
      students_name = input("\t\tPlease enter the student last name: ")
      print(f'\t\tName Received: {students_name}')
      for each in student_records:
        if students_name == each.last_name:
          each.run_report()
    elif record_loop == 2:
      print("\n\t\tFull Student Records Report")
      for each in student_records:
        print(f'\t\tLast Name: {each.last_name.title()}, Date Started: {each.year_started}')
    print("\n\t\tReturning to main menu...")
  return


# Rubric 1 Point:
# Create and display a main menu that prompts to select an option from
# the following options:
#   1) Add a Student
#   2) Update Student Details
#   3) Run Student Report(s)
#   4) Exit
def displayMenu():
  stop_loop = 0
  while stop_loop != 4:
    print("\n\t1) Add a Student Record")
    print("\t2) Update a Student Record")
    print("\t3) Run Student Report(s)")
    print("\t4) Exit\n")
    stop_loop = int(input("\tPlease select an option: "))
    if stop_loop == 1:
      addStudent()
    elif stop_loop == 2:
      updateStudent()
    elif stop_loop == 3:
      runReport()
  return

displayMenu()