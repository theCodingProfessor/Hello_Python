### Lab 7: While Loops and Counter Variables

#### Assignment Overview
In this lab, you will explore the use of `while` loops and counter variables in Python. You will practice controlling loop execution, incrementing and decrementing counter variables, and using user input to manage loop operations.

#### Learning Objectives
- Understand and use `while` loops.
- Practice incrementing and decrementing counter variables.
- Handle user input within a loop to control loop execution.
- Perform arithmetic operations within loops.

#### Instructions: 
Explore the features of a while loop

**7.1) Create File**
- Create a properly formatted Python file named `while_loop.py`

**7.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 7
Description: While Loops and Counter Variables
Author: Your Name Here
"""

```

**7.3) Implement Code**

Print a welcome statement announcing the intention of the lab:
```python
print(f'\nWelcome to Lab 7: While Loops and Counter Variables.')
```

Create the following variables using a single line statement and print their values along with their data types:
```python
counter, min_value, max_value = 0, 1, 10
print(f'\nThe value of counter is {counter} of type {type(counter)}.')
print(f'The value of min_value is {min_value} of type {type(min_value)}.')
print(f'The value of max_value is {max_value} of type {type(max_value)}.')
```

Code a `while` loop that evaluates whether or not the variable `counter` is less than or equal to `max_value`. For each iteration of the loop, print the value of the `counter` and increment the value of the `counter` variable:
```python
print(f'\nWhile loop from {min_value} to {max_value}')
while counter <= max_value:
    print(f'\tThe value of counter is {counter}')
    counter += 1
```

The loop above will exit with a `counter` value of 11. This is because the `counter += 1` does a final addition when the value is 10 (10 + 1 = 11).

Code another `while` loop which decrements the value of the `counter` variable, but switch the order of the print statement and the math statement inside the loop so that the loop properly counts down from ten to one:
```python
# Counter value = 11 (from the previous loop)
print(f'\nWhile loop from {max_value} to {min_value}')
while counter >= min_value:
    counter -= 1
    print(f'\tThe value of counter is {counter}')
```

Declare (on a single line) two variables `user_counter` and `user_sum_total`. Print these variables along with their data types:
```python
user_counter, user_sum_total = 0, 0
print(f'The value of user_counter is {user_counter} of type {type(user_counter)}.')
print(f'The value of user_sum_total is {user_sum_total} of type {type(user_sum_total)}.')
```

Combine the techniques of prompting a user for input and updating the `user_input` value while the `while` loop runs. Code the `while` loop to run until the value received from the user is any negative number (e.g., -1, or -99). Remember to cast the value received to an integer. Inform the user of the rules with the text of your input statement:

```python
print(f"\nUser Defined Counter and Sum-Total Exercise")
user_input = int(input(f'\tEnter a negative number to exit: '))
while user_input >= 0:
    user_sum_total += user_input
    user_counter += 1
    user_input = int(input(f'\tEnter a negative number to exit: '))
```

After the loop exits, report how many times the loop ran, and also report the `user_sum_total`. Ensure that the negative value is not added to the sum:

```python
print(f'\nThe loop ran {user_counter} times.')
print(f'The sum of the positive values entered is {user_sum_total}.')
```

**7.4) Run Your Script**

- Run the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**7.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `while_loop.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of variable declarations, user input, type casting, and `while` loops.
- Accurate use of counters and mathematics operations.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
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

```

<hr>
