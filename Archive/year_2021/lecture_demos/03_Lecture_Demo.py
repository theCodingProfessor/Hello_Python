# Code Demo for 03 Lecture
# Working with Output in Python
# CIS 135 - Code Demo File

# # Sample Print Statements - not formatted
five = 5
# print("print integer literal 5 ", 5)
# print("print integer variable five ", five)
# print(5) # displays 5 to screen
# print('CIS') # displays CIS to screen
# print("CIS 135") # displays CIS 135 to screen

# # Sample pf printing a blank line in python
# print("start")
# print("\n")
# print("end")
# # Sample of printing a newline (blank line) via inline style
# print("\n")
#
# # Sample showing both styles:
# print("Before printing of a blank line")
# print()
# print("Before printing of the blank line")
# print("\nThis is the inline blank line style")

# # Capitalizes the first letter of the first word in a string
# cap_this = "pYTHON programming is FUN.  "
# print("\nCapitalize Python...", cap_this.capitalize())

# # Example of a print statement before a blank input statement:
# print("Type in the score: ")
# score = input()
# print(score)

# # Example of a blank input statement all alone:
# print()
# score = input()
# print(score)

# # Example of an input statement with embedded prompt:
# print()
# score = input("Please input the score: ")
# print(score)

# # Example of an input statement with embedded prompt and newline:
# score = input("\nPlease input the score: ")
# print(score)

# # Example of an input statement that converts the string it receives
# # and saves the value as an integer:
# score = input("\nPlease input the score: ")
# sum = int(score) + int(score)
# print(sum)
# print(type(sum))
# print(type(score))

# # Example of an input statement that converts the string it receives
# # and saves the value as a float:
# score = float(input("\nPlease input the score: "))
# print(score)

# Example of padding space around a numeric value to make it line up properly
# item_one = 10
# item_two = 100
# inventory = "The item number {:3d} is available."
# print(inventory.format(item_one))
# print(inventory.format(item_two))

# Example of padding space around a string value to make it line up properly
# name_one = "Pat"
# name_two = "Patrick"
# player = "Welcome {0:7s} to Python."
# print(player.format(name_one))
# print(player.format(name_two))

# Various examples of string functions available in Python
#
# # Capitalizes the first letter of the first word in a string
# cap_this = "python programming is FUN.  "
# print("\nCapitalize Python...", cap_this.capitalize())

# # Returns "True" if the string contains all letters of the alphabet
# is_all_chars = "python programming is FUN."
# no_space_or_punct = "pythonprogrammingisFUN"
# print("\nTrue or False: is_all_chars is all characters? ", is_all_chars.isalpha())
# print("True or False: no_space_or_punct is all characters? ", no_space_or_punct.isalpha())

# #	Returns "True" if the string contains all digits
# char_1_5 = "1234500"
# print("\nTrue or False: char1_5 is all digits? ", char_1_5.isdigit())

# # Returns a right trimmed value of the string
# clear_this = "python programming is FUN       "
# clear_not = "           python programming is FUN       "
# print("\nClears out the", clear_not.lstrip(), "white space.")
# print("\nClears out the", clear_this.rstrip(), "white space.")

# # Convert each word in a string to Title Case
cap_this = "python programming is FUN.  "
print("\nApply Title Case to cap_this ", cap_this.title())

# # Convert an entire string into UPPER CASE characters
cap_this = "python programming is FUN.  "
print("\nApply UPPER CASE to cap_this ", cap_this.upper())
