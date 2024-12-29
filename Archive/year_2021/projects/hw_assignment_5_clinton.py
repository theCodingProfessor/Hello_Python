# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_5_clinton.py
# CIS-135 Python
# Homework Assignment #5 - Integer Evaluation

# Code Summary:
# This application takes three numbers (integers) from a
# user, and evaluates the numbers to determine the highest
# and lowest of those numbers. The high and low numbers are
# finally printed to the screen.

# Variable Declaration Area:
number_1 = 0
number_2 = 0
number_3 = 0
lowest_number = 0
highest_number = 0

# Welcome the user to the program
print("\nWelcome User")
print("\nThis program requires you to enter three integers (whole numbers).")
print("The highest and lowest numbers are determined and printed.\n")

# Obtain Data from the User
# Prompt user for each integer
number_1 = int(input("\tPlease enter the first integer: "))
number_2 = int(input("\tPlease enter the second integer: "))
number_3 = int(input("\tPlease enter the third integer: "))
print("\tThank you for the data")

# Compute the highest and lowest numbers:
# Compare Values to Determine the Lowest
# Get a result that is the lowest_number
# Set Lowest Number to be the value of number_1
lowest_number = number_1
# Compare if lowest_number is less than number_2
if (lowest_number > number_2):
  # if true: update lowest_number with number_2
  lowest_number = number_2
# Compare if lowest_number is less than number_3
if (lowest_number > number_3):
  # if true: update lowest_number with number_3
  lowest_number = number_3

# Compare Values to Determine the Highest
# Get a result that is the highest_number
# Set Highest Number to be the value of number_1
highest_number = number_1
# Compare if lowest_number is less than number_2
if (highest_number < number_2):
  # if true: update lowest_number with number_2
  highest_number = number_2
# Compare if lowest_number is less than number_3
if (highest_number < number_3):
  # if true: update lowest_number with number_3
  highest_number = number_3

# Display the results to the screen (highest and lowest)
print("\n\tThe lowest number is: ", lowest_number)
print("\tThe highest number is:", highest_number)

# Thank the user
print("\nThank you for using the integer evaluation app.")

