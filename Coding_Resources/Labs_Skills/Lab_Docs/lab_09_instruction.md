### Lab 9: Outer and Inner Loops (Nested Loops)

#### Assignment Overview
In this lab, you will explore the use of nested `for` loops in Python. You will practice incrementing and decrementing nested loops to understand how to handle both loops simultaneously.

#### Learning Objectives
- Understand and use nested `for` loops.
- Practice incrementing and decrementing loops.
- Implement nested loops to manage multiple layers of iteration.

#### Instructions
Explore Loops nested within other Loops

**9.1) Create File**
- Create a properly formatted Python file named `nested_loop.py`

**9.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 9
Description: Outer and Inner Loops (Nested Loops)
Author: Your Name Here
"""

```

**9.3) Implement Code**

Print a welcome statement announcing the intention of the lab:
```python
print(f'\nWelcome to Lab 9: Nested Loops.')
```

Declare on a single line and then print using a formatted print statement these two variables: `stop_up = 4`, `stop_down = 0`:
```python
stop_up, stop_down = 4, 0
print(f'\nThe stop_up variable is {stop_up} of type {type(stop_up)}')
print(f'The stop_down variable is {stop_down} of type {type(stop_down)}')
```

Code an outer `for` loop using the built-in Python `range()` function, with 1 as the first value and `stop_up` as the second parameter value. On the next line (indented), code an inner `for` loop also using the `range` function with 1 as the first value and `stop_up` as the second parameter. On the next indented line print the values of each loop's counters to the screen using formatted print strings and labels for each variable. Include a title/label before the output of the nested loops is displayed to inform the user of the data being shown:
```python
print(f'\nIncrementing Nested Loops')
for out_loop_1 in range(1, stop_up):
    for in_loop_1 in range(1, stop_up):
        print(f'\tOuter Counter {out_loop_1} Inner Loop {in_loop_1}')
    print()
```

Code a decrementing nested loop system. Code the outer loop using the built-in Python `range()` function, with 3 as the first parameter value, `stop_down` as the second parameter, and `-1` as the step (third) parameter value. On the next line (indented), code another inner `for` loop following the same pattern, ensuring that the `for` loop counter variables have different names. Print the values of each of the decrementing loops' counter values to the screen using formatted print strings and labels for each variable. Include a title/label before the output of the nested loops is displayed to inform the user of the data being shown:
```python
print(f'\nDecrementing Nested Loops')
for out_loop_2 in range(3, stop_down, -1):
    for in_loop_2 in range(3, stop_down, -1):
        print(f'\tOuter Counter {out_loop_2} Inner Loop {in_loop_2}')
    print()
```

Notice the `print()` statement on the last line of both nested loop systems. This statement prints a blank line and its indentation is important. The `print()` statement is nested at the same level as the inner `for` loop. This allows the inner loops to print as a group, separated by a blank line, making it easy for the user to identify the nested loop pattern.

**9.4) Run Your Script**

- Execute the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**9.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `nested_loop.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of nested `for` loops.
- Accurate use of incrementing and decrementing loops.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 9
Description: Outer and Inner Loops (Nested Loops)
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 9: Outer and Inner Loops (Nested Loops)')

# Initialize Data
stop_up, stop_down = 4, 0
print(f'\nThe stop_up variable is {stop_up} of type {type(stop_up)}')
print(f'The stop_down variable is {stop_down} of type {type(stop_down)}')

# Count Up Outer and Inner Loop(s)
print(f'\nIncrementing Nested Loops')
for out_loop_1 in range(1, stop_up):
    for in_loop_1 in range(1, stop_up):
        print(f'\tOuter Counter {out_loop_1} Inner Loop {in_loop_1}')
    print()

# Count Down Outer and Inner Loop(s)
print(f'\nDecrementing Nested Loops')
for out_loop_2 in range(3, stop_down, -1):
    for in_loop_2 in range(3, stop_down, -1):
        print(f'\tOuter Counter {out_loop_2} Inner Loop {in_loop_2}')
    print()

```

<hr>
