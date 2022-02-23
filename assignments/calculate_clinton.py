# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# counter_clinton.py
# CIS-135 Python
# Assignment #13 Calculations

# Rubric: 1 Point
# Create a subroutine named addTwo that prompts a user for two numbers,
# adds them together and displays the result to the screen.
def addTwo():
  numOne = int(input("\tPlease enter the first number to add: "))
  numTwo = int(input("\tPlease enter the second number to add: "))
  sum = numOne + numTwo
  print("\tAdding: %d + %d = %d" %(numOne, numTwo, sum))
  input("\tPress enter to continue... \n")
  return

# Rubric: 1 Point
# Create a subroutine named subtractTwo that prompts a user for two
# numbers, subtracts the first from the second and displays the result
# to the screen.
def subtractTwo():
  numOne = int(input("Please enter the first number to subtract: "))
  numTwo = int(input("Please enter the second number to subtract: "))
  difference = numOne - numTwo
  print("Subtracting: %d - %d = %d" %(numOne, numTwo, difference))
  input("Press enter to continue... \n")
  return

# Rubric: 1 Point
# Create a subroutine named divideTwo that prompts a user for two
# numbers, divides the first by the second and displays the result to the screen.
def divideTwo():
  numOne = int(input("Please enter a number for the numerator: "))
  numTwo = int(input("Please enter a number for the denominator: "))
  quotient = numOne / numTwo
  print("Dividing %d %% %d = %d" %(numOne, numTwo, quotient))
  input("Press enter to continue... \n")
  return

# Rubric: 1 Point
# Create a subroutine named productTwo that prompts a user for two
# numbers, multiplies the first by the second and displays the
# result to the screen.
def productTwo():
  numOne = int(input("Please enter the first number to multiply: "))
  numTwo = int(input("Please enter the second number to multiply: "))
  product = numOne * numTwo
  print("Multiplying: %d x %d = %d" %(numOne, numTwo, product))
  input("Press enter to continue... \n")
  return

# Rubric: 1 Point
# Create a main loop, which consistently displays a menu to the screen,
# prompting a user to make a selection, and allows the user to end the
# program by entering 0

selection = 10
while selection != 0:
  print("\nGreetings! Welcome to the Python Calculator")
  print("Please make a selection from the menu below: ")
  print("\t Enter 1) Addition")
  print("\t Enter 2) Subtraction")
  print("\t Enter 3) Division")
  print("\t Enter 4) Multiplication")
  print("\t\t Enter 0 (zero) to exit")
  selection = int(input("Please make your selection: "))
  if (selection == 1):
    addTwo()
  elif (selection == 2):
    subtractTwo()
  elif (selection == 3):
    divideTwo()
  elif (selection == 4):
    productTwo()
  elif (selection == 0):
    print("Goodbye")
  else:
    print("Your input is not valid. Please try again.")
