# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# person_clinton.py
# CIS-135 Python
# Assignment #27 Handling Errors in Python

import person_clinton

# Create a file named instantiate_person.py which makes use of the
# Person class (i.e., import person) using the class file you created
# in Assignment 27 (the name of your file will be unique).

person_directory = []

def addPerson():
  print("\nAdd a New Person")
  first = input("Please enter the person's first name: ")
  last = input("Please enter the person's last name: ")
  food = input("Please enter the person's favorite food: ")
  new_person = person_clinton.Person(first,last,food)
  person_directory.append(new_person)
  print(f'New entry added to the directory.')
  new_person.personal_traits()
  return

def removePerson():
  print("\n\tRemove an entry from the directory ")
  last = input("\tPlease enter the person's last name: ")
  for each in person_directory:
    if last.lower() == each.last_name.lower():
      person_directory.remove(each)
  printDirectory()
  return

def printDirectory():
  print("\nThe entries currently in the directory are:")
  for each in person_directory:
    each.personal_traits()
  return

# Rubric 1 Point: Create a menu driven program which continuously
# loops until the user chooses to exit. The menu should include the
# following options:
# 1) Add a New Person to the People Directory
# 2) Remove a Person from the Dictionary
# 3) Print out the entire People Dictionary
# 4) Exit
def displayMenu():
  stop_loop = 0
  while stop_loop != 4:
    print("\n1) Add a Person to the directory")
    print("2) Remove a Person from the directory")
    print("3) Print out the entire dictionary")
    print("4) Exit")
    stop_loop = int(input("Please select an option: "))
    if stop_loop == 1:
      addPerson()
    elif stop_loop == 2:
      removePerson()
    elif stop_loop == 3:
      printDirectory()
  return

displayMenu()