### Lab 8: For Loops and List Enumeration

#### Assignment Overview
In this lab, you will explore the use of `for` loops, the `range()` function, and the `enumerate()` function in Python. You will practice iterating over ranges and collections, and using enumeration to manage and access list indices.

#### Learning Objectives
- Understand and use `for` loops with the `range()` function.
- Practice iterating over collections like lists and strings.
- Use the `enumerate()` function to access indices in a loop.
- Implement loop control mechanisms like `break`.

#### Instructions
Explore the features of a for loop

**8.1) Create File**
- Create a properly formatted Python file named `for_loop.py`

**8.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 8
Description: For Loops and List Enumeration
Author: Your Name Here
"""

```

**8.3) Implement Code**

Print a welcome statement announcing the intention of the lab:
```python
print(f'\nWelcome to Lab 8: For Loops and List Enumeration.')
```

Code a `for` loop using the built-in Python `range()` function that prints the values from 1 to 10:
```python
print(f'\nFor loop printing values from 1 to 10')
for each in range(1, 11):
    print(f'\tNow at {each}')
```

- Notice that the `range` function prints the value '1', but does not print the value '11'. The first parameter value of `range` is therefore inclusive, and the second parameter value is exclusive, meaning `range` counts up to but not including the number 11.
- Code another `for` loop using `range()`, but this time count down from 10 to 1, and add the third `range` parameter (step value):

```python
print(f'\nFor loop printing values from 10 to 1')
for each in range(10, 0, -1):
    print(f'\tNow at {each}')
```

- Notice that this loop again includes 10 (first parameter value) and counts down to (but ignores 0). The third parameter `-1` is the value decremented with each loop iteration. The third value does not need to be `-1`. Update your decrementing loop passing in `-2` to see the results:

```python
print(f'\nFor loop printing even values from 10 to 1')
for each in range(10, 0, -2):
    print(f'\tNow at {each}')
```

- For loops are not limited to evaluating numeric data and can also be used to iterate collections like strings or words. Create and display the values of a Python list (named `alpha_values`) as follows:
- Code a `for` loop which evaluates any string entered by a user (use an input statement to update a variable named `user_string`) and have it evaluate each item in the collection to see if it is an exact match to any of the values in `alpha_values`:

```python
alpha_values = ["abcd", "efg", "hijk", "lmnop", "qrs", "tuv", "wxyz"]
print(f'\nThe alpha_values are {alpha_values}')

user_string = input(f'\nPlease enter a string to compare to the alpha_values list: ')
for each in alpha_values:
    if each == user_string:
        print(f'\tThe value {user_string} was found.') 
    else:
        print(f'\tThe value {user_string} is different than {each}.')
```

For loops also provide an `enumerate` control device which allows a collection (like `alpha_values`) to be separated from the position (called an index) they maintain in the list. Code another `for` loop using the built-in `enumerate()` function to re-evaluate a user-supplied value against each value in the list. This time implement a `break` statement which will allow the loop to exit (called short-circuit evaluation) if the string is found, but otherwise let the loop run to the end if the value is not found:
```python
user_string = input(f'\nPlease enter a string to compare to the alpha_values list: ')
for index, value in enumerate(alpha_values):
    if value == user_string:
        print(f'\t{user_string} was found at position {index}.')
        break  
    else:
        print(f'\t{user_string} was NOT found at index {index} which has the value {value}')
```

**8.4) Run Your Script**

- Execute the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**8.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `for_loop.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of `for` loops, `range()`, and `enumerate()`.
- Accurate use of loops to iterate over ranges and collections.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
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

# Print Loop with decreasing values (demonstrates decrementing step)
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

# This DOES NOT stop if the user string is found 
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

```

<hr>
