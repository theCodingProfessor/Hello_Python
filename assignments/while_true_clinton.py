# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# while_true_clinton.py
# CIS-135 Python
# Assignment #9
# # # Lab 9

# Get while_yes and enter Loop
# Initial Value received from input is a string value
# print("While Looping Exercises")
#while_yes = input("Yes or No? Input y for yes, or n for no")

# # While Yes Loop
# while_yes = 'y'
# while while_yes == 'y' or while_yes == "Y":
#   print("'While-Yes Loop' runs as long as 'y' is entered, any other character exits the loop")
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

# While False Loop
while_false = False  # This is a boolean value (True or False)
while(while_false != True):
  print("While False loop will exit if True (#1) is entered")
  t_f = int(input("Enter 1 for True, or 2 for False "))
  if t_f == 1:
    while_false = True
  else:
    print("")
print("Exited While False Loop Successfully")

