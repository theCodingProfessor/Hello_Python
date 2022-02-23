# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# sum_total_clinton.py
# CIS-135 Python
# Assignment #14 Sum Total Calculations

# Rubric: 1 Point
# Create a function named askAgain that contains a while loop that asks a user
# to enter any number, or 0 (the number zero) to exit the loop.

# # Simple Implementation
# def askAgain():
#   get_input = 1
#   sub_total = 0
#   while get_input != 0:
#     get_input = int(input("\tPlease enter a number, or enter 0 (zero) to exit: "))
#     sub_total += get_input
#     print("\tGrand total so far = : ", sub_total)
#   return sub_total
#
# print("Welcome to the Sum-Total Python App")
# grand_total = askAgain()
# print("The grand total is ", grand_total)

def askAgain():
  sub_total = 0
  loop_counter = 0
  get_input = int(input("\tPlease enter a number, or enter 0 (zero) to exit: "))
  while get_input != 0:
    sub_total += get_input  # sub_total = sub_total + get_input
    loop_counter += 1
    print("\tLoop count:", loop_counter, "Running grand total so far: ", sub_total)
    get_input = int(input("\tPlease enter a number, or enter 0 (zero) to exit: "))
  return loop_counter, sub_total

print("Welcome to the Advanced Sum-Total Python App")
count_loop, grand_total = askAgain()
print("The loop ran", count_loop, "times, with a grand total of", grand_total)
