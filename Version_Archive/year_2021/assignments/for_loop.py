# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# for_loop_clinton.py
# CIS-135 Python
# For Loop Lecture

# Syntax Coding_Resources:
# https://www.w3schools.com/python/python_for_loops.asp

# Python Docs:
# https://docs.python.org/3/tutorial/controlflow.html#for-statements
# https://docs.python.org/3/library/stdtypes.html#iterator-types
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/tutorial/controlflow.html#pass-statements
# https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
# https://docs.python.org/3/tutorial/controlflow.html#the-range-function
# https://docs.python.org/3/tutorial/index.html
# https://docs.python.org/3/

# While Loop   or a   For Loop
# x = 11
# while (x == 10):
#   print("this is true")
#   x = 10
# else:
#   print("not true found")

# For Loop that processes a literal iterable
# print("\nFor Loop that processes a literal iterable")
# for each in ['a','b','c']:
#   print("\t", each)

# # For Loop that processes an iterable variable
# print("\nFor Loop that processes an iterable variable; a list here")
# xyz = ['x','y','z']
# for each in xyz:
#   print("\t", each)
#   print(xyz)
#   xyz.append(each)
#   input()

# For Loop that processes some items from an iterable variable
# print("\nFor Loop that processes some items from an iterable variable")
# hijklmnopqrst = ['h','i','j','k','l','m','n','o','p','q','r','s','t']
# for each in hijklmnopqrst[2:-3]:
#   print("\t", each)

# For Loop processes some items from iterable variable with slice
# print("\nFor Loop processes some items from iterable variable with slice")
# hijklmnopqrst = ['h','i','j','k','l','m','n','o','p','q','r','s','t']
# for each in hijklmnopqrst[1:9:3]:
#   print("\t", each)

# # # For Loop with one integer in range parameter
# print("\nFor Loop with one integer in range parameter")
# for each in range(3):
#   print("\t", each)

# # # For Loop with two integers in range parameter
# print("\nFor Loop with two integers in range parameter")
# for each in range(10,15):
#   print("\t", each)

# # For Loop with three integers in range parameter
# print("\nFor Loop with three integers in range parameter")
# for each in range(20,30,2):
#   print("\t", each)

# # ETL Extract (visit and get), Transform (compute) and Load (save elsewhere)
#
# # For Loop with a conditional statement
# # This makes use of the Python modulo operator - return remainder
# # here is the number / 2 == 0 (no remainder) then print the number
# # This will print only even numbers
# print("\nFor Loop with modulo conditional statement")
# for each in range(1,11):
#   if each % 2 == 0:
#     print("\t", each)

# # # For Loop with a conditional statement - implements pass
# # # This makes use of the Python modulo operator - return remainder
# # # here is the number / 2 == 0 (no remainder) then pass
# # # otherwise print 'odd number found' and the number
# print("\nFor Loop with a conditional statement - implements pass")
# for each in range(1,11):
#   if each % 2 == 0:
#     pass
#   else:
#     print("\tOdd number found", each)

# # # # For Loop with a conditional statement implementing break
# print("\nFor Loop with a conditional statement implementing break")
# for each in range(1,10):
#   print("now at:", each)
#   if each == 3:
#     print("\tFound",each, "found a continue in the loop.")
#     continue

# START - single entrance
# STOP - single exit

y = 'y'
if( y == 'y' or y=="Y" ):
  print("Y")
