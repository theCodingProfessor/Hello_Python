"""
Module Name: Programming Lab 6
Description: Compound Conditional Evaluations using AND/OR
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 6: Compound Conditional Evaluations using AND/OR')

# Initialize data and report values
the_min = 0
the_max = 256
print(f'\nData Created:')
print(f'\tthe_min = {the_min} as data-type {type(the_min)}.')
print(f'\tthe_max = {the_max} as data-type {type(the_max)}.')

# Use an input statement to prompt a user and to receive/assign value
user_value = int(input(f'\nPlease enter a value to be compared against the_min and the_max values: '))
print(f'\tValue received = {user_value} as data-type {type(user_value)}.')

# AND: Chained Comparison (Modern Pythonic Approach):
print(f'\nAND: Chained Comparison - Pythonic')
if the_min < user_value <= the_max:
    print(f'\tThe value {user_value} is greater than {the_min} and also less than or equal to {the_max}.')
elif user_value < the_min:
    print(f'\tThe value {user_value} is less than {the_min}.')
else:
    print(f'\tThe value {user_value} is greater than {the_max}.')

# AND: Separate Comparisons (Traditional Approach)
print(f'\nAND: Separate Comparisons - Traditional')
if the_min < user_value and user_value <= the_max:
    print(f'\tThe value {user_value} is greater than {the_min} and also less than or equal to {the_max}.')
elif user_value < the_min:
    print(f'\tThe value {user_value} is less than {the_min}.')
elif user_value > the_max:
    print(f'\tThe value {user_value} is greater than {the_max}.')

# OR: Separate Comparisons (Logical OR) with Short-Circuit Evaluation
print(f'\nOR: Separate Comparisons - Short Circuit')
if user_value < the_min or user_value > the_max:
    print(f'\tThe value {user_value} is either less than {the_min} or greater than {the_max}')
else:
    print(f'\tThe value {user_value} is between {the_min} and {the_max}')
