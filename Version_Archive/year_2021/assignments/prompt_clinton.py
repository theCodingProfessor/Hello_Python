# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# prompt_clinton.py
# CIS-135 Python
# Assignment #7

# syntax  input_keyword(parenthesis,quote[your data]quote,parenthesis)
# syntax  input("your data")
# my_name = input("Please enter your name: ")
# print("hello,", my_name)

# Print a message to the screen asking for string value
name_given_str = input("Please input your name: ")
print("The value you typed was,", name_given_str, "thank you,", name_given_str)

# Print a message to the screen asking for integer value
number_given_int = int(input("Please enter either zero or one: "))
print("The value you typed was,", number_given_int, "thank you,", name_given_str)
print("The data type() of your input is ", type(number_given_int))

# Print a message to the screen asking for integer value
color_given_str = input("What is the best color? ")
print("You are right %s, the best color is %s" % (name_given_str, color_given_str) )

# # #

# Lab 8: Prompt evaluate Answers

# # Print a message asking for yes ('y') or no ('n') from a user
# yesNo1 = input("Yes or No? Type y for yes, or n for no")
# yesNo2 = input("Yes or No? Type y for yes, or n for no")

# # declare yes no function
# def yes_no():
#   y_n = input("Yes or No? Type y for yes, or n for no")
#   print("Inside the function your input was: ", y_n)
#   return
#   yes_no()

# # Print a message to the screen asking for integer value
# yesNo1 = input("Yes or No? Type y for yes, or n for no")
# if yesNo1 == 'y' or yesNo1 == 'Y':
#   print("Yes recieved!")
#   print("Thank you, %s. " % (name_given_str) )

# # Print a message evaluate if, elif (else if)
# yesNo1 = input("Yes or No? Type y for yes, or n for no")
# if yesNo1 == 'y' or yesNo1 == 'Y':
#   print("Yes recieved!")
# elif yesNo1 == 'n' or yesNo1 == 'N':
#   print("No recieved!")
# else:
#   print("Neither yes or nor was received.")

# # # Lab 9

# Get while_yes and enter Loop
# Initial Value received from input is a string value
# print("While Looping Exercises")
#while_yes = input("Yes or No? Input y for yes, or n for no")

# # While Yes Loop
# while_yes = 'y'
# while while_yes == 'y' or while_yes == "Y":
#   print("While yes runs as long as 'y' is entered, any other character exits the loop")
#   while_yes = input("Type y to continue, or any other character to exit.")
# print("Exited Loop Successfully")

# # While True Loop
# while_true = True  # This is a boolean value (True or False)
# while(while_true == True):
#   print("While True loop will run until False (#2) is entered")
#   t_f = int(input("Enter 1 for True, or 2 for False "))
#   if t_f == 1:
#     pass
#   elif t_f == 2:
#     while_true = False
# print("While True Loop Successfully")

# # While False Loop
# while_false = False  # This is a boolean value (True or False)
# while(while_false != True):
#   print("While False loop will exit if True (#1) is entered")
#   t_f = int(input("Enter 1 for True, or 2 for False "))
#   if t_f == 1:
#     while_false = True
#   else:
#     print("Exited While False Loop Successfully")
