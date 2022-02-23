# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# scope_clinton.py
# CIS-135 Python
# Assignment #12 Scope

# Rubric: 1 Point.
# Create a function named enterGrid which takes a single
# argument, a numeric variable called flynnAge.
# a) Inside the function declare a variable named
# flynnAge and set it equal to the value of the variable plus twenty.
# b) Print the words "Flynn's age inside the grid is" along
# with the updated value of flynnAge.
# c) Do not return any value from the function.
def enterGrid(flynnAge):
  flynnAge = flynnAge + 20
  print("Flynn's age inside the grid is", flynnAge)
  return

flynnAge = 27
print("\nFlynn's age before calling enterGrid = %g" % flynnAge)
enterGrid(flynnAge)
print("Flynn's age after calling enterGrid = %g" % flynnAge)

# Rubric: 1 Point.
# Create a function named getName which takes one variable
# called lastISO
# a) Inside the function declare a variable named userName
# and set it equal to the variable lastISO that was passed
# into the function.
# b) Print userName to the screen.
# c) Update the variable userName to the value "Quorra".
# d) Print out the updated variable.
# e) Make the function return the updated (userName)
# variable to the caller.

def getName(lastISO):
  userName = lastISO
  print("\tuserName is: ", userName)
  userName = "Quorra"
  print("\tuserName is: ", userName)
  return userName

lastISO = "unknown"
print("\nThe original value of lastISO is %s" % lastISO)
lastISO = getName(lastISO)
print("The value of lastISO is now %s" % lastISO)
#print("The value of userName is %s" % userName)

