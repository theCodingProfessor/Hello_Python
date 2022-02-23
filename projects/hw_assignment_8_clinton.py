# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_8_clinton.py
# CIS-135 Python
# Homework Assignment #8 - Data Dictionary Application

# Code Summary: This data dictionary application allows a user to look
# up and add words to a dictionary using Python. The program
# continuously displays a main menu with three options, Add New Item,
# Lookup Item or Exit.

# Change Log:
# Fully implemented and tested 1) When in the lookup function, and we have
# a term to add pass that term to the addFunction as a function parameter
# overload, and streamline data request from lookup function.

# Start addData function  (the_dictionary)
def addData(the_dictionary, the_term):
  # Implement streamlined call from lookup function
  if len(the_term) != 0:
    # Handle call from lookup function where term is passed in
    print("\n\t\t\tThe term received to define is", the_term)
    # handle updating the definition
    the_value = input("\t\t\tPlease enter the definition for the term: ")
    the_dictionary.update({the_term: the_value})
  else:
    # Term is not yet known
    # Print "Enter a new term to add to the dictionary:"
    print("\n\t\tEnter a new term to add to the dictionary: ")
    new_term = input("\t\tor enter 'exit' to return to main menu: ")
    # while new_term is not 'exit'
    while new_term != 'exit':
      # if new_term is in the_dictionary:
      if new_term in the_dictionary:
        # Print 'This term is already in the dictionary."
        print("\t\tThis term is already in the dictionary.")
        # Print 'It is defined as: ... "
        print("\t\tIt is defined as:", the_dictionary[new_term])
        # yes_no = prompt "Would you like to replace this definition"
        yes_no = input("\n\t\tEnter 'y' to replace this definition: ")
        if yes_no.lower() == 'y':
          #  new_definition = input "Please enter the new definition"
          new_definition = input("\n\t\tPlease enter the new definition: ")
          # Save the new definition:
          the_dictionary[new_term] = new_definition
      else:
        # new_definition = input "Please enter the definition for this term"
        new_definition = input("\n\t\tPlease enter the new definition: ")
        # Save the new definition:
        the_dictionary.update({new_term: new_definition})
      # Print "Enter a new term to add to the dictionary:"
      # new_term = input "or enter 'exit' to return to main menu"
      print("\n\t\tEnter a new term to add to the dictionary,")
      new_term = input("\t\tor enter 'exit' to return to main menu: ")
  return the_dictionary

# Start getData function (the_dictionary)
def getData(the_dictionary):
  # Print "Enter a term to lookup or"
  # the_term = input "enter 'exit' to return to main menu"
  print("\n\t\tEnter a term to lookup or enter 'exit to")
  the_term = input("\t\treturn main menu: ")
  # while the_term is not 'exit'
  while the_term != 'exit':
    # if the_term is in the_dictionary:
    if the_term in the_dictionary:
      # print the value of the term from the_dictionary
      print("\n\t\tThis term already exists, and is defined as:")
      print("\t\t\t", the_dictionary[the_term])
    else:
      print("\n\t\tThe word was not found in the dictionary.")
      print("\t\tWould you like to add this word to the dictionary?")
      #  yes_no = prompt "Enter 'y' for yes or 'n' for no"
      yes_no = input("\t\tEnter 'y' to add this word: ")
      if yes_no.lower() == 'y':
        the_dictionary = addData(the_dictionary, the_term)
        print("\t\tThank you. That term is now in the dictionary.\n")
    # Print "Enter a term to lookup or"
    # the_term = input "enter 'exit' to return to main menu"
    print("\n\t\tPlease enter another term to lookup or type in 'exit'")
    the_term = input("\t\tto return to the main menu: ")
  return the_dictionary

# Start main function
def main():
  # the_dictionary = Python dictionary
  the_dictionary = {}
  the_term = ""
  user_input = -99
  # Print a welcome message to the user
  print("\nWelcome to the Python Dictionary Application")
  # Print a short description of the program
  print("\nThis program allows you to lookup or add new words to the dictionary.")
  # While user_input not equal to quit == 3:
  while user_input != 3:
    # Display Menu
    # print: Option 1) Lookup Term
    print("\n\tOption 1) Lookup a Term")
    # print: Option 2) Add New Term
    print("\tOption 2) Add a New Term")
    # print: Option 3) Quit
    print("\tOption 3) Quit")
    user_input = int(input("\t\tPlease select an option: "))
    # if user_input is 1: call
    if user_input == 1:
      the_dictionary = getData(the_dictionary)
    # if user_input is 2: call
    elif user_input == 2:
      the_dictionary = addData(the_dictionary, the_term)
    elif user_input != 3:
      print("\t\tThat is not a valid selection, please try again.")
    # if user_input is 3: quit the program
  print("\nThank you for using the Python Dictionary Application")
  # End main function
  return

main()
