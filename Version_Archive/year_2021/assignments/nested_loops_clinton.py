# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# nested_loops_clinton.py
# CIS-135 Python
# Assignment #20 Counters in Loops

# Rubric 1 Point:
# Create and call a function named incrementLoop that contains a loop,
# inside of another loop, which prints out a incremented ascending
# list of numbers.
def incrementLoop():
  outer_counter = 1
  while outer_counter <= 3:
    inner_counter = 1
    while inner_counter <= 3:
      print(f'\tOuter Counter {outer_counter}, Inner Counter {inner_counter}')
      inner_counter += 1
    outer_counter += 1
  return
print("\nCounting Up with Nested Loops")
incrementLoop()

# Rubric 1 Point: Create and call a function named decrementLoop
# that contains a loop, inside of another loop, which prints out a
# decremented list of numbers.
def decrementLoop():
    outer_counter = 3
    while outer_counter > 0:
      inner_counter = 3
      while inner_counter > 0:
        print(f'\tOuter Counter {outer_counter}, Inner Counter {inner_counter}')
        inner_counter -= 1
      outer_counter -= 1
    return
print("\nCounting Down with Nested Loops")
decrementLoop()
print()

# Rubric 3 Points: Create and call a function named stopWatch which
# models the function of a timer, displaying seconds and minutes
# (use at least two loops - properly nested), which continuously
# print until the updated time until a user chooses to exit
# (typically accomplished by pressing Control + C, or Control + X.

# import required library to use time.sleep()
import time

def stopWatch():
  second, minute = 60,-1
  while second == 60:
    second = 0
    if minute == -1: minute = 0 # lambda
    else: minute += 1
    while second <= 59:
      if second <= 9:
        print(f'Timer : {minute}:0{second}')
      else:
        print(f'Timer : {minute}:{second}')
      time.sleep(1)
      second += 1
  return
stopWatch()
