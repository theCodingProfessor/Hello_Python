### Lab 10: Functions as Reusable/Callable Code

#### Assignment Overview
In this lab, you will explore creating and using functions in Python to make your code more reusable and organized. You will define and call functions to perform various tasks, and practice passing data to and returning data from functions.

#### Learning Objectives
- Understand and use function declarations and calls.
- Practice defining and using functions with and without parameters.
- Implement functions to return data based on inputs.

#### Instructions
Explore functions which act as reusable code blocks.

**10.1) Create File**
- Create a properly formatted Python file named `function_calls.py`

**10.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 10
Description: Functions as Reusable Code
Author: Your Name Here
"""

```

**10.3) Implement Code**

Define a function named `main`, and inside this function, create a welcome statement that announces the intention of the lab:
```python
def main():
    print(f'\nWelcome to Lab 10: Functions as Reusable Code.')
    return   


main()
  
```

- Notice that `main()` appears twice. The first time it is preceded by the keyword `def`, short for 'define', which declares the function. The second time `main()` is used on its own line without any words before or after it. The second usage the 'function call' and it is how we activate (or call) the function. The indentation following the first use is important, and the `return` statement, while technically not required, provides a clear end to the function.
- Functions in Python require two blank lines before and after them. Ensure that the `main()` call has two blank lines before it and a single blank line at the end.
- Define three additional functions: `just_print`, `add_and_return`, and `empty_or_not`. These functions should be declared before the `main` function so they are in scope (available in memory) before they are used. Stub each function initially:

```python
def just_print():
    return


def add_and_return():
    return


def empty_or_not():
    return
```

Revisit the `just_print` function to add a formatted print message:
```python
def just_print():
    print(f'\tInside the just_print function.')
    return
```

Next, update the `add_and_return` function to take a numeric value as its only parameter and return the value added to itself:
```python
def add_and_return(number_in):
    return number_in + number_in
```

Also update the `empty_or_not` function to take a string value as its parameter and check if the string is empty or not. Return 1 if the string has data, and 0 if it is empty. Include a multi-line comment describing the function:
```python
def empty_or_not(string_in):
    """
    This function takes a string variable and
    checks it to determine if it is an empty string or not.
    If the string has data (is valid), the variable status
    is updated to true (or 1). The value of status (updated or not)
    is returned to the caller.
    """
    status = 0
    if len(string_in) > 0:
        status = 1
    return status
```

Update the `main` function to call each of the three functions, passing data and catching data as required:
```python
def main():
    print(f'\nWelcome to Lab 10: Functions as Reusable Code.')

    # Call just_print() does not take or return data
    print(f'\nNow calling just_print()')
    just_print()

    # Call add_and_return(int) takes and returns integer
    # Be sure to catch the returned value.
    print(f'\nNow calling add_and_return(int)')
    catch_twenty = add_and_return(10)
    print(f'\tadd_and_return(10) returned {catch_twenty}')

    # Call empty_or_not(valid_string)
    # Be sure to catch the returned value.
    print(f'\nNow calling empty_or_not(string)')
    catch_one = empty_or_not('all good')
    print(f'\tempty_or_not("all good") returns {catch_one}')

    return


main()

```

**10.4) Run Your Script**

- Execute the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**10.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `function_calls.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of functions.
- Accurate use of function parameters and return values.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 10
Description: Functions as Reusable/Callable Code
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def just_print():
    print(f'\tInside the just_print function.')
    return


def add_and_return(number_in):
    return number_in + number_in


def empty_or_not(string_in):
    """
    This function takes a string variable and
    checks it to determine if it is an empty string or not.
    If the string has data (is valid), the variable status
    is updated to true (or 1). The value of status (updated or not)
    is returned to the caller.
    """
    status = 0
    if len(string_in) > 0:
        status = 1
    return status


def main():
    print(f'\nWelcome to Lab 10: Functions as Reusable Code.')

    # Call just_print() does not take or return data
    print(f'\nNow calling just_print()')
    just_print()

    # Call add_and_return(int) takes and returns integer
    # Be sure to catch the returned value.
    print(f'\nNow calling add_and_return(int)')
    catch_twenty = add_and_return(10)
    print(f'\tadd_and_return(10) returned {catch_twenty}')

    # Call empty_or_not(valid_string)
    # Be sure to catch the returned value.
    print(f'\nNow calling empty_or_not(string)')
    catch_one = empty_or_not('all good')
    print(f'\tempty_or_not("all good") returns {catch_one}')

    return


main()

```

<hr>
