### Lab 4: User Input and Data Types

#### Assignment Overview
In this lab, you will explore different data types in Python and learn how to manipulate them using built-in functions. You will practice using the `int()`, `float()`, and `type()` functions to understand how Python handles different data types and typecasting.

#### Learning Objectives
- Understand and use the `int()`, `float()`, and `type()` functions in Python.
- Learn about string concatenation and typecasting.
- Practice using formatted print statements to display variable values and types.

#### Instructions
Whitespace is important: print() is not the same as print ()

**4.1) Create File**
- Create a properly formatted Python file named `data_types.py`

**4.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 4
Description: User Input and Data Types
Author: Your Name Here
"""

```

**4.3) Implement Code**
- Print a welcome message using a formatted print string. 
- Create three variables: `string_twenty`, `integer_ten`, and `float_five`, and assign them the values `"20"`, `10`, and `5.0`, respectively.
- Print each variable and its type using a formatted print statement and the `type()` function:
```python
print(f'\nWelcome to Lab 4: Understanding Data Types}')

string_twenty = "20"
integer_ten = 10
float_five = 5.0

print(f'string_twenty is {string_twenty} and is of type {type(string_twenty)}')
print(f'integer_ten is {integer_ten} and is of type {type(integer_ten)}')
print(f'float_five is {float_five} and is of type {type(float_five)}')
```

Use three formatted print statements to add each variable to itself and display the results:
```python
print(f'string_twenty added to itself is {string_twenty + string_twenty}')
print(f'integer_ten added to itself is {integer_ten + integer_ten}')
print(f'float_five added to itself is {float_five + float_five}')
```

Note that the 'addition' of strings does not produce a mathematically valid result. This type of string 'addition' is called concatenation.

Strings cannot be mathematically added to themselves or to other data types without manipulating them first. This process is called casting. Use the Python built-in `int()` or `float()` functions to cast the string data to an integer or float, then add them together:
```python
print(f'string_twenty cast to int and added to itself is {int(string_twenty) + int(string_twenty)}')
print(f'string_twenty cast to float and added to itself is {float(string_twenty) + float(string_twenty)}')
```

Different data types, such as `int` and `float`, may automatically be upcast or downcast by the Python interpreter without requiring you to use the `int()` or `float()` functions. Add `integer_ten` and `float_five` together, and print the result and its type:
```python
print(f'integer_ten added to float_five is {integer_ten + float_five} and is of type {type(integer_ten + float_five)}')
```

Using print statements, attempt to add `string_twenty` to both `integer_ten` and `float_five`, first casting the string data to integer and then float data types respectively (four print statements total):
```python
print(f'string_twenty cast to int and added to integer_ten is {int(string_twenty) + integer_ten}')
print(f'string_twenty cast to float and added to integer_ten is {float(string_twenty) + integer_ten}')
print(f'string_twenty cast to int and added to float_five is {int(string_twenty) + float_five}')
print(f'string_twenty cast to float and added to float_five is {float(string_twenty) + float_five}')
```

**4.4) Run Your Script**

- Run the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening variable declarations.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**4.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `data_types.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of variable declarations, typecasting, and formatted print statements.
- Accurate use of the `int()`, `float()`, and `type()` functions.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
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

# Use formatted print statements with inline mathematics statement
print(f'\nInline Addition:')
print(f'\tstring_twenty + string_twenty = {string_twenty + string_twenty} because concatenation is not addition')
print(f'\tinteger_ten + integer_ten = {integer_ten + integer_ten}')
print(f'\tfloat_five + float_five = {float_five + float_five}')

# Inline casting (explicit)
print(f'\nInline Casting')
print(f'\tint(string_twenty) + int(string_twenty) = {int(string_twenty) + int(string_twenty)}')
print(f'\tfloat(string_twenty) + float(string_twenty) = {float(string_twenty) + float(string_twenty)}')

# Inline casting (implicit)
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

# Downcasting float to int
print(f'\nDowncasting Numeric (float to int')
print(f'\tinteger_ten + int(float_five) = {integer_ten + int(float_five)}')

```

<hr>
