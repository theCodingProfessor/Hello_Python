### Lab 6: Compound Conditional Evaluations using AND/OR

#### Assignment Overview
In this lab, you will explore multiple conditional evaluations in a single statement using Python's `AND` and `OR` syntax. You will practice writing and debugging compound conditional statements.

#### Learning Objectives
- Understand and use compound conditional statements with `AND` and `OR` operators.
- Practice handling user input and type casting.
- Enhance skills in writing and debugging complex conditional logic.

#### Instructions
Explore multiple evaluations in a single statement

**6.1) Create File**
- Create a properly formatted Python file named `and_or_evaluation.py`

**6.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 6
Description: Multiple Conditional Evaluations using AND/OR
Author: Your Name Here
"""

```

**6.3) Implement Code**

Print a welcome statement announcing the intention of the lab:

```python
print(f'\nWelcome to Lab 6: Multiple Conditional Statements using AND/OR.')
```

Define the following variables and print their values, including their data types:

```python
the_min = 0
the_max = 256
print(f'\nThe value of the_min is {the_min} of type {type(the_min)}.')
print(f'The value of the_max is {the_max} of type {type(the_max)}.')
```

Use an input statement to instruct the user to enter an integer value, cast the value received to an integer, and assign it to a new variable named `user_value`. Print a verification of the value received along with the data type:

```python
user_value = int(input(f'\nPlease enter a value to be compared against the_min and the_max values: '))
print(f'The value received is {user_value} of type {type(user_value)}.')
```

Use a compound `AND` evaluation statement to determine if the `user_value` is greater than `the_min` and also less than or equal to `the_max`. Print the results:

```python
if the_min < user_value <= the_max:
    print(f'\tThe value entered {user_value} is greater than {the_min} and also less than or equal to {the_max}.')
elif user_value < the_min:
    print(f'\tThe value entered {user_value} is less than {the_min}.')
else:
    print(f'\tThe value entered {user_value} is greater than {the_max}.')
```

Another way this statement could have been written to accomplish the same goal:

```python
if the_min < user_value and user_value <= the_max:
    print(f'\tThe value entered {user_value} is greater than {the_min} and also less than or equal to {the_max}.')
elif user_value < the_min:
    print(f'\tThe value entered {user_value} is less than {the_min}.')
elif user_value > the_max:
    print(f'\tThe value entered {user_value} is greater than {the_max}.')
```

Use a compound `OR` evaluation statement to determine the differences between the `user_value` against `the_min` and `the_max` values. Print the results:
```python
if user_value < the_min or user_value > the_max:
    print(f'The value entered {user_value} is either less than {the_min} or greater than {the_max}')
else:
    print(f'The value entered {user_value} is between {the_min} and {the_max}')
```

**6.4) Run Your Script**
- Execute the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**6.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `and_or_evaluation.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of variable declarations, user input, type casting, and compound conditional statements.
- Accurate use of `AND` and `OR` operators.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
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

```

<hr>
