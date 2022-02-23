# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_6_clinton.py
# CIS-135 Python
# Homework Assignment #6 - Integer Average App

# Code Summary:
# This application prompts a user to enter integers until
# they input the integer -99. Once the loop exists the
# application will compute the average of all the input
# received, and print the results out to the screen.

# Variable Declaration Area:
new_integer = 0
sum_of_inputs = 0
count_of_inputs = 0
average_of_input = 0.00

# Introduction: Welcome user and introduce the application
print("\nWelcome to the Integer Average Calculator")
print("\n\tThis program asks the user to input integers, until the integer -99 ")
print("\tis entered. Then it computes the average of all the integers entered,")
print("\tand prints out the result.\n")

# Acquire Data
# Get the initial data from the user (prime the new_integer)
# cast the data received to an integer value
new_integer = int(input("\t\tPlease a whole number or -99 to exit: "))
while new_integer != -99:
  # update the sum-total
  sum_of_inputs += new_integer
  # update count of inputs
  count_of_inputs += 1
  # get the next integer
  new_integer = int(input("\t\tEnter another integer or -99 to exit: "))
print("\t\tExiting Input Loop: Thank you for the data.\n")

#Compute the Average:
# Compute Average (1 + 2 + 3) / 3 == 6/3 == 2
# Watch for float value results
# consider casting float(sum_of_inputs), float(count_of_inputs)
if (count_of_inputs != 0):
  average_of_input = float(sum_of_inputs) / float(count_of_inputs)
else:
  average_of_input = 0.00

#Display Results to the user:
print("\tThe total number of integers found is:", count_of_inputs)
print("\tThe total sum of the input is:", sum_of_inputs)
print("\tComputing Results: sum_of_inputs / count_of_inputs are, {}/{}".format(sum_of_inputs, count_of_inputs))
print("\n\tThe Average Computed is: {}".format(round(average_of_input,2)))
print("\nThank you for using the Integer Average Calculator.")
