### Lab 2: Comments, Variables, and Formatted Printing

#### Assignment Overview
In this lab, you will practice using comments, variables, and formatted printing in Python. This will help you better understand how to document code and display dynamic content.

#### Learning Objectives

- Learn how to use different types of comments in Python.
- Understand how to declare and use variables.
- Utilize formatted strings to display dynamic content.

#### Instructions
A single blank line MUST be at the bottom of a .py module

**2.1) Create File**
Create a new Python file named `code_comments.py` and ensure a single blank line is at the end of this file. 

**2.2) Add Metadata (header/comments)**

Use the proper 'module level docstring' which carries a unified format across all the source code files. Include the following module-level comment with the proper details at the top of your source code file.
```python
"""
Module Name: Programming Lab 2
Description: Comments, Variables, and Formatted Printing
Author: Your Name Here
Date: Optional
"""

```

**2.3) Implement Code**
Print a welcome message using a formatted print string. For example:
```python
print(f'Welcome to Lab 2: Understanding Code Comments')
```

Insert a triple-single-quoted multi-line comment with a description of when to use this style of comment. For example:

```python
'''
Triple-single-quoted comments are often used for docstrings or large blocks of text. 
They are useful for documentation purposes or multi-line comments. 
'''
```

Insert a triple-double-quoted multi-line comment with a description of when to use this style of comment. For example:

```python
""" 
Triple-double-quoted comments are similar to triple-single-quoted comments 
and are used for the same purposes. They are commonly used for docstrings 
and are more compatible with other programming languages. 
"""
```

Interaction with Users: 

- Declare a string variable named `my_name` and assign it your preferred name. For example:
- Use a formatted print statement to print a label along with your preferred name by referencing the `my_name` variable. For example:

```python
my_name = 'Your Preferred Name'
print(f'Your preferred name is: {my_name}')
```

**2.4) Run Your Script**

- Execute the script in your IDE to ensure that the correct output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the print function and the parentheses).

#### Submission
- Submit a single source code file named `code_comments.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Accurate use and placement of comments.
- Correct implementation of variables and formatted printing.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 2
Description: Comments, Variables, and Formatted Printing
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 2: Comments, Variables, and Formatted Printing')

'''
Triple-single-quoted comments are often used for docstrings or large blocks of text. 
They are useful for documentation purposes or multi-line comments. 
'''

""" 
Triple-double-quoted comments are similar to triple-single-quoted comments 
and are used for the same purposes. They are commonly used for docstrings 
and are more compatible with other programming languages. 
"""

my_name = 'Your Preferred Name'
print(f'Your preferred name is: {my_name}')

# Explore the built-in string methods
print(f'Your preferred name is: {my_name.upper()}')
print(f'Your preferred name is: {my_name.capitalize()}')
print(f'Your preferred name is: {my_name.title()}')
print(f'Your preferred name is: {my_name.count("r")}')

```

<hr>
