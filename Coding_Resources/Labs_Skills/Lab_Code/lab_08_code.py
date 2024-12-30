"""
Module Name: Programming Lab 8
Description: For Loops and List Enumeration
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 8: For Loops and List Enumeration')

# Print Loop with ascending values (demonstrates range)
print(f'\nFor loop printing values from 1 to 10')
for each in range(1, 11):
    print(f'\tNow at {each}')

# Print Loop with decreasing values (demonstrates a decrementing step)
print(f'\nFor loop printing values from 10 to 1')
for each in range(10, 0, -1):
    print(f'\tNow at {each}')

# Print Loop with even values (demonstrates step parameter)
print(f'\nFor loop printing even values from 10 to 1')
for each in range(10, 0, -2):
    print(f'\tNow at {each}')

# Initialize Data
alpha_values = ["abcd", "efg", "hijk", "lmnop", "qrs", "tuv", "wxyz"]
print(f'\nThe alpha_values are {alpha_values}')

# This does `NOT` stop if the user string is found
user_string = input(f'\nPlease enter a string to compare to the alpha_values list: ')
for each in alpha_values:
    if each == user_string:
        print(f'\tThe value {user_string} was found.')
    else:
        print(f'\tThe value {user_string} is different than {each}.')

# Demonstrates enumerate(), this DOES stop if the user string is found
user_string = input(f'\nPlease enter a string to compare to the alpha_values list: ')
for index, value in enumerate(alpha_values):
    if value == user_string:
        print(f'\t{user_string} was found at position {index}.')
        break
    else:
        print(f'\t{user_string} was NOT found at index {index} which has the value {value}')
