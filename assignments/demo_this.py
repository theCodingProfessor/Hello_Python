# Code Testing
# CIS 135 - Quiz 11

# def updateInteger(num1,num2):
#   sum = num1 + num2
#   return sum
#
# def getText():
#   sometext = input("Type a string: ")
#   return sometext
#
# def main():
#   num1, intVariable = 0,0
#   while num1 < 2:
#     intVariable = updateInteger(num1,num1+1)
#     num1+=1
#   stringVariable = getText()
#   print(f'String received was, {stringVariable}')
#   print(f'Final value of integers is {intVariable}')
#   return
#
# main()

# five = 5
# print(5)
# print(five)
# print("\n")
# print(five)

# # Capitalizes the first letter of the first word in a string
# cap_this = "python programming is FUN.  "
# print("\nCapitalize Python...", cap_this.capitalize())

# Returns "True" if the string contains all letters of the alphabet
is_all_chars = "python programming is FUN."
no_space_or_punct = "pythonprogrammingisFUN"
print("\nTrue or False: is_all_chars is all characters? ", is_all_chars.isalpha())
print("True or False: no_space_or_punct is all characters? ", no_space_or_punct.isalpha())

#	Returns "True" if the string contains all digits
char_1_5 = "12345"
print("\nTrue or False: char1_5 is all digits? ", char_1_5.isdigit())

# Returns a right trimmed value of the string
clear_this = "python programming is FUN       "
print("\nClears out the", clear_this.rstrip(), "white space.")

# Convert each word in a string to Title Case
cap_this = "python programming is FUN.  "
print("\nApply Title Case to cap_this ", cap_this.title())

# Convert an entire string into UPPER CASE characters
cap_this = "python programming is FUN.  "
print("\nApply UPPER CASE to cap_this ", cap_this.upper())

print()
print()
print()
print()
print()
print()
print()
print()
print()


# print("\nStrip out the extra white space at the end? ", cap_this.rstrip())
# # Returns a right trimmed value of the string
#
# print("\nApply Title Case to cap_this ", cap_this.title())
# # Convert each word to Title Case
#
# print("\nApply UPPER CASE to cap_this ", cap_this.upper())
# #Convert the entire string into UPPER CASE characters


# item_one = 10
# item_two = 100
# inventory = "The item number {0:3d} is available."
# print(inventory.format(item_one))
# print(inventory.format(item_two))

# name_one = "Pat"
# name_two = "Patrick"
# player = "Welcome {0:7s} to Python."
# print(player.format(name_one))
# print(player.format(name_two))
