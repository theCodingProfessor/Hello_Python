# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# counter_clinton.py
# CIS-135 Python
# Assignment #10 Counters in Loops

# Rubric: 1 Point
# Use a python while loop that continuously runs as long as a user inputs the
# response 'y' for yes. Inside the loop increment the value of a counter
# variable, printing out the value of the counter with each loop cycle.
# After the loop finally exits, print the value of the counter again.
control_variable_1 = 'y'
counter_position_1 = 0
while control_variable_1 == 'y':
  counter_position_1 = counter_position_1 + 1
  control_variable_1 = input("Counter 1 at %d, enter 'y' to continue: " %(counter_position_1))
  # optional implementation
  # print("The counter is", counter_position_1)
  # control_variable_1 = input("Enter 'y' to continue, or any other input to exit: ")

# Rubric: 1 Point
# Use a traditional while loop that continuously runs as long as a user inputs the
# response 'y' for yes. Inside the loop increment the value of a counter variable,
# printing out the value of the counter with each loop cycle. After the
# loop finally exits, print the value of the counter again, this time making sure
# that the value displayed on the last run of the loop is the same as the final
# value printed once the loop is finished.

control_variable_2 = 'y'
counter_position_2 = 0
while control_variable_2 == 'y':
  counter_position_2 = counter_position_2 + 1
  control_variable_2 = input("Counter 2 at %d, enter 'y' to continue: " %(counter_position_2))
print("The counter 2 ended at position: ", counter_position_2)

# Rubric: 1 Point
# Use a while loop to print the values counting up from 1 to 10.
count_up = 1
while count_up < 11:
  print("Counter 3 =", count_up)
  count_up = count_up + 1

# Rubric: 1 Point
# Use a while loop to print the values counting down from 10 to 1.
count_down = 10
while count_down > 0:
  print("Counter 4 =", count_down)
  count_down = count_down - 1

# # Extra Credit:
# # Wrap each loop into a function (see the next assignment - Lab 11).
#
# def countdown():
#   count_down = 10
#   while count_down > 0:
#     print("Counter 4 =", count_down)
#     #print(count_down)
#     count_down = count_down - 1
#   return
#
# def countup():
#   count_up = 1
#   while count_up < 11:
#     print("Counter 3 =", count_up)
#     #print(count_up)
#     count_up = count_up + 1
#   return
#
# def print_inside():
#   control_variable_1 = 'y'
#   counter_position_1 = 0
#   while control_variable_1 == 'y':
#     counter_position_1 = counter_position_1 + 1
#     control_variable_1 = input("Counter 1 at %d, enter 'y' to continue: " % (counter_position_1))
#   return
#
# def print_outside():
#   control_variable_2 = 'y'
#   counter_position_2 = 0
#   while control_variable_2 == 'y':
#     counter_position_2 = counter_position_2 + 1
#     control_variable_2 = input("Counter 2 at %d, enter 'y' to continue: " % (counter_position_2))
#   print("Counter 2 ended at position ", counter_position_2)
#   return
#
# print_inside()
# print_outside()
# countup()
# countdown()
