### Lab 3: User Input and Program Flow

#### Assignment Overview
In this lab, you will practice handling user input and controlling program flow in Python. You will learn how to prompt the user for data, compare it against a static value, and report on the validity of the input.

#### Learning Objectives
- Understand how to prompt the user for input in Python.
- Learn to use conditional statements to evaluate user input.
- Practice reporting valid and invalid input using formatted print statements.

#### Instructions
Follow the workflow below as a programming lab.
Use a `sandbox` (different .py file) for code-tinkering and idea exploration

**3.1) Create File**
- Create a properly formatted Python file named `prompt_user.py`

**3.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 3
Description: User Input and Program Flow
Author: Your Name Here
"""

```

**3.3) Implement Code**
Print a welcome message using a formatted print string. Following the welcome statement insert four single-line comments denoting the program flow:
```python
print(f'\nWelcome to Lab 3: User Interaction.')
# A) Prompt user for data
# B) Compare data against static value
# C) Report valid input
# D) Report invalid input
```

Workflow: 

- Under the 'Prompt user for data' comment, code an `input` statement that prompts the user to enter a string (e.g., a word or name), and assign the received data to a variable named `user_data`:
- Indent the 'Report valid input' comment, and then on the next line (also indented to the same level), code a formatted print statement that announces the string is valid and injects the received data into the print statement:
- On the next line (not indented), use the `else:` statement with a single-line trailing comment ('Report invalid input'):
- Indent the line below this, and use a formatted print statement to announce the data was not valid:
- Under the 'Compare data' comment, code an `if` statement that evaluates the string's length using the built-in Python `len()` function. Valid data will have a length greater than zero:

```python
# A) Prompt user for data
user_data = input("Prompt 2: Please enter a word or name: ")
# B) Compare data against static value
if len(user_data) > 0:  # C) Report valid input
    print(f'\tThe data received, {user_data} is valid.')
else:  # D) Report invalid input
    print(f'\tThe data received is not valid.')
```

**3.4) Run Your Script**

- Run the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening input statement.
- Ensure there is a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

#### Submission
- Submit a single source code file named `prompt_user.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Accurate use of comments to denote program flow.
- Correct implementation of user input and conditional statements.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 3
Description: User Input and Program Flow
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 3: User Input and Program Flow')

# Code block without comments
user_data = input("\nPrompt 1: Please enter a word or name: ")
if len(user_data) > 0:
    print(f'\tThe data received, {user_data} is valid.')
else:
    print(f'\tThe data received is not valid.')

# Code block with comments
# A) Prompt user for data
user_data = input("Prompt 2: Please enter a word or name: ")
# B) Compare data against static value
if len(user_data) > 0:  # C) Report valid input
    print(f'\tThe data received, {user_data} is valid.')
else:  # D) Report invalid input
    print(f'\tThe data received is not valid.')

```

<hr>
