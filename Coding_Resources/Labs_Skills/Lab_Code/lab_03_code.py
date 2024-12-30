"""
Module Name: Programming Lab 3
Description: User Input and Program Flow
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 3: User Input and Program Flow')

# Code block without comments
user_data = input("\nPrompt 1: Please enter a word or name: ")
if len(user_data) > 0:
    print(f'\tThe data received, {user_data} is valid.')
else:
    print(f'\tThe data received is not valid.')

# Code block with comments
# A) Prompt user for data
user_data = input("Prompt 2: Please enter a word or name: ")
# B) Compare data against static value
if len(user_data) > 0:  # C) Report valid input
    print(f'\tThe data received, {user_data} is valid.')
else:  # D) Report invalid input
    print(f'\tThe data received is not valid.')
