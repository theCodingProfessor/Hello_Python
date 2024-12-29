"""
Module Name: Programming Lab 7
Description: While Loops and Counter Variables
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 7: While Loops and Counter Variables')

# Initialize data and report values
counter, min_value, max_value = 0, 1, 10
print(f'\nInitial Data:')
print(f'\tcounter = {counter} of type {type(counter)}.')
print(f'\tmin_value = {min_value} of type {type(min_value)}.')
print(f'\tmax_value = {max_value} of type {type(max_value)}.')

# Use a while loop (sentinel value, incrementing counter)
print(f'\nWhile loop from {min_value} to {max_value}')
while counter < max_value:
    counter += 1
    print(f'\tThe value of counter is {counter}')

# Use a while loop (sentinel value, decrementing counter)
# Counter value = 11 (from the previous loop)
print(f'\nWhile loop from {max_value} to {min_value}')
while counter >= min_value:
    print(f'\tThe value of counter is {counter}')
    counter -= 1

# Initialize new data and report values
user_counter, user_sum_total = 0, 0
print(f'\nNew Data:')
print(f'\tThe value of user_counter is {user_counter} of type {type(user_counter)}.')
print(f'\tThe value of user_sum_total is {user_sum_total} of type {type(user_sum_total)}.')

# Combine techniques as sum-total calculator
print(f"\nUser Defined Counter and Sum-Total Exercise")
user_input = int(input(f'\tEnter a negative number to exit: '))
while user_input >= 0:
    user_sum_total += user_input
    user_counter += 1
    user_input = int(input(f'\tEnter a negative number to exit: '))
print(f'\nThe loop ran {user_counter} times.')
print(f'The sum of the positive values entered is {user_sum_total}.')
