"""
Module Name: Programming Lab 4
Description: User Input and Data Types
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 4: User Input and Data Types')

# Initialize data and report values
string_twenty = "20"
integer_ten = 10
float_five = 5.0
print(f'\nData Created:')
print(f'\tstring_twenty = {string_twenty} of type {type(string_twenty)}')
print(f'\tinteger_ten = {integer_ten} of type {type(integer_ten)}')
print(f'\tfloat_five = {float_five} of type {type(float_five)}')

# Use formatted print statements with inline mathematics statements
print(f'\nInline Addition:')
print(f'\tstring_twenty + string_twenty = {string_twenty + string_twenty} because concatenation is not addition')
print(f'\tinteger_ten + integer_ten = {integer_ten + integer_ten}')
print(f'\tfloat_five + float_five = {float_five + float_five}')

# Inline casting (explicit)
print(f'\nInline Casting - explicit')
print(f'\tint(string_twenty) + int(string_twenty) = {int(string_twenty) + int(string_twenty)}')
print(f'\tfloat(string_twenty) + float(string_twenty) = {float(string_twenty) + float(string_twenty)}')

# Inline casting (implicit)
print(f'\nInline Casting - implicit')
print(f'\tinteger_ten + float_five = {integer_ten + float_five} and is of type {type(integer_ten + float_five)}')

# Upcasting converting string to numeric
print(f'\nUp Casting String')
print(f'\tint(string_twenty) + integer_ten = {int(string_twenty) + integer_ten}')
print(f'\tfloat(string_twenty) + integer_ten = {float(string_twenty) + integer_ten}')
print(f'\tint(string_twenty) + float_five {int(string_twenty) + float_five}')
print(f'\tfloat(string_twenty) + float_five = {float(string_twenty) + float_five}')

# Upcasting converting int to float
print(f'\nUpcasting Numeric')
print(f'\tfloat(integer_ten) + integer_ten = {float(integer_ten) + integer_ten}')
print(f'\tfloat(integer_ten) + float_five = {float(integer_ten) + float_five}')

# Down casting float to int
print(f'\nDown casting Numeric (float to int)')
print(f'\tinteger_ten + int(float_five) = {integer_ten + int(float_five)}')
