# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# if_else_clinton.py
# CIS-135 Python
# Assignment #8

# Lab 8: Prompt evaluate Answers

name_given_str = input('Please enter your name: ')

# # Print a message asking for yes ('y') or no ('n') from a user
# yesNo1 = input("Yes or No? Type y for yes, or n for no ")
# yesNo2 = input("Yes or No? Type y for yes, or n for no ")

# # declare yes no function
# def me_yes_no():
#   y_n = input("Yes or No? Type y for yes, or n for no ")
#   print("Inside the function your input was: ", y_n)
#   return
# me_yes_no()

# # Print a message to the screen asking for integer value
# yesNo1 = input("Yes or No? Type y for yes, or n for no ")
# if yesNo1 == 'y' or yesNo1 == 'Y':
#   print("Yes is recieved!")
#   print("Thank you, %s. " % (name_given_str) )
# else:
#   print("y was not the answer")

# Print a message evaluate if, elif & else
yesNo2 = input("Yes or No? Type y for yes, or n for no ")
if yesNo2 == 'y' or yesNo2 == 'Y':
  print("Yes recieved!")
elif yesNo2 == 'n' or yesNo2 == 'N':
  print("No recieved!")
else:
  print("Neither yes nor no was received.")

