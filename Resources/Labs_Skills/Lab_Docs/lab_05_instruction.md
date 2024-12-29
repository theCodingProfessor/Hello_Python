### Lab 5: Exploring Conditional Statements

#### Assignment Overview
In this lab, you will explore the use of conditional statements in Python, specifically `if`, `elif`, and `else` statements. You will practice writing multiple forms of these statements to compare user input against a predefined value.

#### Learning Objectives

- Understand and use `if`, `elif`, and `else` statements in Python.
- Learn how to handle user input and type casting.
- Practice writing and debugging conditional statements with different comparison operators.

#### Instructions
In Python after using the : (colon syntax) indent the code block that follows.

**5.1) Create File**
- Create a properly formatted Python file named `if_elif_else.py`

**5.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 5
Description: Exploring Conditional Statements
Author: Your Name Here
"""

```

**5.3) Implement Code**
Print a welcome statement announcing the intention of the lab:
```python
print(f'\nWelcome to Lab 5: Multiple Condition Statements')
```

Create an integer variable `year` with the value `2025` and print its value to the user:
```python
year = 2025
print(f'The year variable is set to {year}')
```

Prompt the user to enter a value which will be compared to the value of the `year` variable. Cast the input value to an integer and assign it to the variable `user_year`:
```python
user_year = int(input(f"\nPlease enter a four-digit year: "))
```

Print a confirmation to the user displaying both the data received and its type:
```python
print(f'The data you entered is {user_year} of type {type(user_year)}')
```

Code an `if`, `elif`, `else` statement to determine if the user input is greater than, equal to, or less than `year`:
```python
if user_year > year:
    print(f'Your entry {user_year} is greater than {year}')
elif user_year == year:
    print(f'Your entry {user_year} is equal to {year}')
elif user_year < year:
    print(f'Your entry {user_year} is less than {year}')
else:
    print(f'This statement should never be reached.')
```

Modify the conditional statement to check for greater-than-or-equal-to:
```python
if user_year >= year:
    print(f'Your entry {user_year} is greater than or equal to {year}')
elif user_year < year:
    print(f'Your entry {user_year} is less than {year}')
else:
    print(f'This statement should never be reached.')
```

Modify the conditional statement to check for less-than-or-equal-to:
```python
if user_year > year:
    print(f'Your entry {user_year} is greater than {year}')
elif user_year <= year:
    print(f'Your entry {user_year} is less than or equal to {year}')
else:
    print(f'This statement should never be reached.')
```

Modify the conditional statement to check for not-equal-to:
```python
if user_year != year:
    print(f'Your entry {user_year} is not equal to {year}')
else:
    print(f'Your entry {user_year} is neither greater than nor less than {year}')
```

**5.4) Run Your Script**

- Execute the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**5.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `if_elif_else.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of variable declarations, user input, type casting, and conditional statements.
- Accurate use of `if`, `elif`, and `else` statements with different comparison operators.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
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

```

<hr>
