### Application 2: Functions and Data Calculator
**Topics:** Data Types, Casting, User-Defined Functions, Parameter Lists, Return Values 

<hr>
### 1. Objective
**Purpose:**  
- This assignment asks you to create a complete design document that includes a detailed pseudocode representation of the algorithm..
- Use semantic self-documenting names for variables and functions  
- Translate the pseudocode into Python code.

**Pathway:**
1) Describe the algorithm for a simple application using pseudocode, and include it with the design document template.
2) The pseudocode should cover the entire program logic, including all function calls and the main control flow. In addition describe each function and it's unique implementation/steps. Use the START to END style with every function.
3) The design document with the pseudocode is the `specification` Code the working Python application from this specification.

#### Calculator Options:
Experimenting in a topic area of interest to you is encouraged (but not required).
Select a concept and define its design (algorithm) document before creating code.
-- IP subnet masks (networking)
-- Buy-or-sell investment (finance)
-- Electric capacity of a circuit (engineering)
-- Scientific computations (using `math`) (data science)

<hr>
### 2. Learning Outcomes

- **Design:** Create pseudocode that represents five unique python functions, including a main() function to implement the logic presented to the user through a user-interface/menu.  
- **Develop:** Translate the algorithm (pseudocode) into a working Python program.
- **Troubleshoot:** Identify and correct logical errors during coding, documenting them in a Change Log.

<hr>

### 3. Assignment Instructions

**Part 1-1: Initialize a Design Document**  
- **Working Title:** Provide a meaningful title for your app.
- **Author Information:** Include your name.
- **Description:** Write a short description of the algorithm or app.
- **Representation(s):** Pseudocode

**Part 1-2: Define the Algorithm as Pseudocode
- Declare a program START 
- For each Function in the Application:
	- Declare a START first_function
		- Define each step (first, next... last... etc., as needed)
	- Declare an END first_function
- When all the functions have been START name, STOP name, defined, declare a program STOP 

**Part 2: Create the Application**  

- **Translation:** Convert the design document into a working Python app..
- **Change Log:** If you encounter logic errors during coding (e.g., steps out of order, missing loops), make the necessary corrections in the code. Document these changes in a multi-line comment section titled **"Change Log"** at the top of your code.

<hr>

### 4. Submission Requirements

- **Design Document:** Submit a design document. Markdown (.md), PDF (.pdf) or MS Word (.docx) document types.
- **Python Code:** Submit a Python file (.py). Add a change log section (if applicable).

<hr>

### 5. Success Criteria

- **Design Document:**  
  - The required header is present
  - Visual indentation of functions and code logic in pseudocode.
  - Visual separation of each function in the pseudocode document

- **Python Code:**  
  - Correct implementation of the design.
  - Functionality and correctness of the code.
  - Appropriate handling of errors and logic issues.

- **Change Log:**  
  - Accurate and clear documentation of any issues encountered and the changes made.

<hr>

### 6. Sample as `The Math Calculator`

**Design Document Example:**

**My Math App**  
- **App Type:** Education, Self Improvement
- **Author:** Clinton Garwood  
- **August 2024** 
- **Description:** 
    This application presents the user with a menu that includes the following options:
        1) Add
        2) Subtract
        3) Multiply
        4) Exit
    The menu operates in a continuous loop. When options 1, 2, or 3 are selected, the user is prompted to enter two numbers. These numbers are then passed to the corresponding functions (add_numbers(), subtract_numbers(), multiply_numbers()), which perform the calculations and return the result.

<hr>

**Algorithm as Markdown:**

```markdown

Start main function:
    Print "Welcome to the Python Math App." 
    Loop forever:
        Display the menu options
        Get the user's choice
        If the choice is 1, 
            Call the add_numbers function and print the result
        If the choice is 2, 
            Call the subtract_numbers function and print the result
        If the choice is 3, 
            Call the multiply_numbers function and print the result
        If the choice is 4, 
            Print "Exiting..." and break the loop
        Otherwise
            Print "Invalid choice. Please select again."
    Print "Thank you for using the Python Math App." 
End main function

Start display_menu function:
    Print "1) Add"
    Print "2) Subtract"
    Print "3) Multiply"
    Print "4) Exit"
End display_menu function

Start get_user_choice function:
    Ask the user for their choice and return it as an integer
End get_user_choice function

Start add_numbers function:
    Ask the user for the first number
    Ask the user for the second number
    Call print_result function(first, second, "+", (first + second))
    Return the sum of the two numbers (first + second)
End add_numbers function

Start subtract_numbers function:
    Ask the user for the first number
    Ask the user for the second number
    Call print_result function(first, second, "-", (first - second))
    Return the difference between the two numbers (first - second)
End subtract_numbers function

Start multiply_numbers function:
    Ask the user for the first number
    Ask the user for the second number
    print_result function(first, second, "*", (first * second))
    Return the product of the two numbers (first * second)
End multiply_numbers function

Start print_result function(first, second, operator, result):
    Print "{first} {operator} {second} = {result}
End print_result function


```

<hr>

Sample Pseudocode Document - Pythonic 

My Math App
App Type: Calculator, Productivity
Author: Clinton Garwood
Date: August 2024
License: MIT 

```markdown
Main Function

function main():
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 1:
            result = add_numbers()
            print_result(result)
        elif choice == 2:
            result = subtract_numbers()
            print_result(result)
        elif choice == 3:
            result = multiply_numbers()
            print_result(result)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

Supporting Functions

function display_menu():
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Exit")

function get_user_choice():
    return int(input("Select an option: "))

function add_numbers():
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    return num1 + num2

function subtract_numbers():
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    return num1 - num2

function multiply_numbers():
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    return num1 * num2

function get_number_input(prompt):
    return float(input(prompt))

function print_result(result):
    print("The result is: ", result)

```

<hr>

**Sample Application as Python Code** 

```python
"""  
Sample App: The Math App  
Description: This app does addition, subtraction and multiplication.  
Author: Clinton Garwood  
Date: August 2024  
License: MIT """  
  
  
def main():  
    print(f'Welcome to the Python Math App.')  
    result = 0  
    while True:  
        display_menu()  
        user_choice = get_user_choice()  
        if user_choice == '1':  
            result += add_numbers()  
        elif user_choice == '2':  
            result += subtract_numbers()  
        elif user_choice == '3':  
            result += multiply_numbers()  
        elif user_choice == '4':  
            print(f'\tExiting... ')  
            break  
        else:  
            print(f'\tInvalid choice. Please select again.')  
    print(f'\nThank you for using the Python Math App.')  
    return  
  
  
def display_menu():  
    print(f'\n\t1) Add')  
    print(f'\t2) Subtract')  
    print(f'\t3) Multiply')  
    print(f'\t4) Exit')  
    return  
  
  
def get_user_choice():  
    user_choice = input("\tPlease select: ")  
    return user_choice  
  
  
def add_numbers():  
    first_number = float(input("\n\tEnter first number: "))  
    second_number = float(input("\tEnter second number: "))  
    print_result(first_number, second_number, "+", (first_number * second_number))  
    return first_number + second_number  
  
  
def subtract_numbers():  
    first_number = float(input("\n\tEnter first number: "))  
    second_number = float(input("\tEnter second number: "))  
    print_result(first_number, second_number, "-", (first_number - second_number))  
    return first_number - second_number  
  
  
def multiply_numbers():  
    first_number = float(input("\n\tEnter first number: "))  
    second_number = float(input("\tEnter second number: "))  
    print_result(first_number, second_number, "*", (first_number * second_number))  
    return first_number * second_number  
  
  
def print_result(first, second, operator, result):  
    print(f"\t{first} {operator} {second} = {result}")  
    return  
  
  
main()

```

<hr>
