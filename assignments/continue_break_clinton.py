# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# continue_break_clinton.py
# CIS-135 Python
# Assignment #21 Counters in Loops

# Rubric 1 Point:
# Create (but do not independently call) a function named breakOut that
# implements a break statement with a for-range loop (runs from 1 to 10)
# which breaks out (exits) the loop when the value 5 is found. Do not
# print the number 5
def breakOut():
  print("\t\tInside breakOut function")
  for x in range(1,11):
    if x==5:
      break
    else:
      print(f'\t\t{x}')
  return

# Rubric 1 Point:
# Create (but do not independently call) a function named continueOn
# that implements a continue statement in a for-range loop (runs from
# 1 to 10) which prints all of the values found except for 5.
def continueOn():
  print("\t\tInside continueOn function")
  for x in range(1,11):
    if x==5:
      continue
    else:
      print(f'\t\t{x}')
  return

# Rubric 1 Point:
# Create and call a function named easyPass that simply implements the
# pass keyword as a placeholder for code in the function. We call this
# kind of function a stub, a function-stub, or a stub of a function.
def easyPass():
  print("\t\tInside easyPass function")
  pass
  return

# Rubric 2 Point:
# Create and call a function named mainMenu which which displays a menu
# for the user to call the other functions described above. Allow the
# user to run the functions as many times as they like, while allowing
# them to exit the program by selecting that option from the menu.
def mainMenu():
  selection = 0
  while selection != 4:
    print("\nWelcome to break, continue, pass function caller.")
    print("\tOption 1: Run Break Function")
    print("\tOption 2: Run Continue Function")
    print("\tOption 3: Run Pass Function")
    print("\tOption 4: Exit")
    selection = int(input("\nPlease make a selection from the menu "))
    if selection == 1:
      breakOut()
    elif selection == 2:
      continueOn()
    elif selection == 3:
      easyPass()
  return

mainMenu()