### Lab 11: Passing a Function as a Parameter

#### Assignment Overview
In this lab, you will explore the concept of passing function calls as parameters to other functions. This technique is known as **higher-order functions**. You will define and use functions that take other functions as parameters, demonstrating how functions can interact and be composed in Python.

#### Learning Objectives
- Understand and implement higher-order functions.
- Practice defining and calling functions that return values or use values from other functions.
- Explore the concept of variable scope and the difference between variable names and values.

#### Instructions
Explore additional features of Python User Defined Functions (UDF)

**11.1) Create File**
- Create a properly formatted Python file named `function_scope.py`

**11.2) Add Metadata (header/comments)**
- At the top of your file, include the following comments (do not indent comments):
```python
"""
Module Name: Programming Lab 11
Description: Higher-Order Functions
Author: Your Name Here
"""

```

**11.3) Implement Code**
Define a function named `main`, and inside this function, create a welcome statement that announces the intention of the lab:
```python
def main():
    print(f'\nWelcome to Lab 11: Passing a Function as a Parameter.')
    return   


main()

```

Notice that `main()` appears twice. The first time it is preceded by the keyword `def`, short for 'define', which declares the function. The second time `main()` is used on its own line without any words before or after it. This is the 'function call' and it is how we activate (or call) the function. The indentation is important, and the `return` statement, while technically not required, provides a clear end to the function.

Before the `main` function definition, create three function stubs with the following names: `multiverse_0`, `multiverse_1`, and `multiverse_2`:
```python
def multiverse_0(visitor):
    return visitor


def multiverse_1(visitor):
    return f'{visitor} from Multiverse 1'


def multiverse_2(visitor):
    return f'There is no escape from Multiverse 2'
```

- These functions demonstrate different ways data can be passed to and returned from functions.
- The first three function calls are simple and simply pass a string value. The `multiverse_0` function simply passes the data through, the variable name inside the function goes out of scope (is lost) when the function ends. The `multiverse_1` function returns a formatted concatenated string that includes the passed parameter. The `multiverse_2` function returns a fixed string literal.

- Update the `main` function to prompt the user for their preferred name, assign the value to a variable named `user_name`, and print the value received. Also code a call to multiverse_1 passing user_name in as the parameter value again, but this time make the call inside a formatted print statement. This demonstrates the feature of being able to pass a function call into an injected formatted print statement placeholder. Repeat this pattern to call each of the other two functions in the same fashion.
```python
def main():
    print(f'\nWelcome to Lab 11: Passing a Function as a Parameter.')

    user_name = input('Please enter your preferred name: ')
    print(f'\nYou entered: {user_name}')

    print(f'\nSimple Function Callers >> Values')
    print(f'\tmultiverse_0({user_name}) returns >> {multiverse_0(user_name)}')
    print(f'\tmultiverse_1({user_name}) >> {multiverse_1(user_name)}')
    print(f'\tmultiverse_2({user_name}) >> {multiverse_2(user_name)}')

    print(f'\nNested Function Callers >> Values')
    print(f'\tmultiverse_0(multiverse_1({user_name})) >> {multiverse_0(multiverse_1(user_name))}')
    print(f'\tmultiverse_0(multiverse_2({user_name})) >> {multiverse_0(multiverse_2(user_name))}')
    print(f'\tmultiverse_0(multiverse_1(multiverse_2({user_name}))) >> {multiverse_0(multiverse_1(multiverse_2(user_name)))}')

    return

```

- The last three function calls demonstrate the ability to pass a function call into a function as a parameter value. 
- In multiverse_0 a nested function call to multiverse_1 is used with user_name as its parameter is explained with a formatted print statement showing the result of the nested function call.
- In multiverse_0 a nested function call to multiverse_2 with user_name as its parameter is explained with a formatted print statement showing the result of the nested function call.
- In multiverse_0 giving it a nested function call to multiverse_1, which itself takes a nested function call to multiverse_2 with user_name as its parameter is explained with a formatted print statement showing the result of the nested function calls.

**11.4) Run Your Script**
- Run the script in your IDE to ensure that the proper output is printed to the screen.
- Ensure there is a single blank line between the metadata and the opening print statement.
- Ensure there is
- a single blank line at the end of the source code file.
- Make sure there are no syntax errors, warnings, or issues (such as extra whitespace or spaces between the function name and parentheses).

**11.5) Resolve Issues, Warnings, and Errors**
- Check and resolve any syntax errors, warnings, or other issues that may arise during execution.

#### Submission
- Submit a single source code file named `function_scope.py`.

#### Assessment Criteria
- Proper file naming and adherence to instructions.
- Correct implementation of functions.
- Accurate use of higher-order functions.
- No syntax errors, warnings, or issues in the code.

#### Additional Notes
- Double-check that your script works as intended before submission.
- Ensure that comments and code are clear and properly formatted.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 11
Description: Higher-Order Functions: Passing Functions as Parameters
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def multiverse_0(visitor):
    return visitor


def multiverse_1(visitor):
    return f'{visitor} from Multiverse 1'


def multiverse_2(visitor):
    return f'There is no escape from Multiverse 2'


def main():
    print(f'\nWelcome to Lab 11: Passing a Function as a Parameter.')

    user_name = input('Please enter your preferred name: ')
    print(f'\nYou entered: {user_name}')

    print(f'\nSimple Function Callers >> Values')
    print(f'\tmultiverse_0({user_name}) returns >> {multiverse_0(user_name)}')
    print(f'\tmultiverse_1({user_name}) >> {multiverse_1(user_name)}')
    print(f'\tmultiverse_2({user_name}) >> {multiverse_2(user_name)}')

    print(f'\nNested Function Callers >> Values')
    print(f'\tmultiverse_0(multiverse_1({user_name})) >> {multiverse_0(multiverse_1(user_name))}')
    print(f'\tmultiverse_0(multiverse_2({user_name})) >> {multiverse_0(multiverse_2(user_name))}')
    print(f'\tmultiverse_0(multiverse_1(multiverse_2({user_name}))) >> {multiverse_0(multiverse_1(multiverse_2(user_name)))}')

    return


main()

```

<hr>