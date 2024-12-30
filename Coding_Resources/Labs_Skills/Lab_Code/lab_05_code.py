"""
Module Name: Programming Lab 5
Description: Exploring Conditional Statements
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 5: Exploring Conditional Statements')

# Initialize data and report values
year = 2025
print(f'\tThe year variable is set to {year}')

# Assign user_year int-cast value received as string from user
user_year = int(input(f"\nPlease enter a four-digit year: "))
print(f'\tYou entered {user_year} of type {type(user_year)}')

# Compare Values using if, else if (elif) and else
# Comparisons (greater-than, equal-to, less-than, else)
print(f'\nComparisons (greater-than, equal-to, less-than, else)')
if user_year > year:
    print(f'\t{user_year} is greater than {year}')
elif user_year == year:
    print(f'\t{user_year} is equal to {year}')
elif user_year < year:
    print(f'\t{user_year} is less than {year}')
else:
    print(f'This statement should never be reached.')

# Comparisons (greater-than-or-equal-to, less-than, else)
print(f'\nComparisons (greater-than-or-equal-to, less-than, else)')
if user_year >= year:
    print(f'\t{user_year} is greater than or equal to {year}')
elif user_year < year:
    print(f'\t{user_year} is less than {year}')
else:
    print(f'This statement should never be reached.')

# Comparisons (greater, less-than-or-equal-to, else)
print(f'\nComparisons (greater, less-than-or-equal-to, else)')
if user_year > year:
    print(f'\t{user_year} is greater than {year}')
elif user_year <= year:
    print(f'\t{user_year} is less than or equal to {year}')
else:
    print(f'This statement should never be reached.')

# Comparisons (not-equal-to, else)
print(f'\nComparisons (not-equal-to, else)')
if user_year != year:
    print(f'\t{user_year} is not equal to {year}')
else:
    print(f'\t{user_year} is neither greater than nor less than {year}')
