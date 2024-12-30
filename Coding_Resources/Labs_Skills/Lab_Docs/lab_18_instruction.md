### Lab 18: "Read and Format Data in Files"

#### Assignment Overview
In this lab, you will extend your work with file management techniques.

#### Learning Objectives
- Practice reading and writing data to files in Python.
- Use file handling functions to count lines, append data, and confirm the contents of a file.
- Implement loop and function calls to manage file content.

#### Instructions

**18.1) Create File**
- Create a properly formatted Python file named `file_read.py`.

**18.2) Define Main Function**
- Create and call a function named `main` that takes no data and returns no data.
- Inside `main`, introduce the program and pass a file-name string the function `append_to_ten("data_file.data")` inside `main`.
```python
def main():
    print(f'\nWelcome to Lab 18: Read and Format File Data')

    # Prompt user for the filename append to ten
    append_to_ten("data_file.data")

    return
```

**18.3) Define Supporting Functions**
- Define the following functions with appropriate multi-line comments describing their purpose, parameters, and return values:

**18.3.1) Function: `line_counter`**
- Purpose: Counts the total number of lines in the specified file.
- Parameters: `file_name` (string)
- Returns: Integer value of the line count.
- Implementation:
  - Use Python's built-in `open()` function to read (`'r'` mode) the file.
  - Use a loop to count the total number of lines.
  - Return the integer value of the line count.
```python
def line_counter(file_name):
    """
    Counts the total number of lines in the specified file.
    :param file_name: Name of the file (string)
    :return: Number of lines in the file (integer)
    """
    with open(file_name, 'r') as file:
        counter = sum(1 for line in file)
    return counter
```

**18.3.2) Function: `append_file`**
- Purpose: Appends a line of text to the file, indicating the updated line count.
- Parameters: `file_name` (string), `counter` (integer)
- Returns: None
- Implementation:
  - Use Python's built-in `open()` function in append mode (`'a'`).
  - Write a line of text indicating the updated line count.
  - Close the file.
```python
def append_file(file_name, counter):
    """
    Appends a line of text to the file, indicating the updated line count.
    :param file_name: Name of the file (string)
    :param counter: Current number of lines in the file (integer)
    :return: None
    """
    with open(file_name, 'a') as file:
        file.write(f"data_file.data had {counter} lines of data, and now it has {counter + 1}\n")
```

**18.3.3) Function: `confirm_append`**
- Purpose: Prints the contents of the file to the screen.
- Parameters: `file_name` (string)
- Returns: None
- Implementation:
  - Use Python's built-in `open()` function to read (`'r'` mode) the file.
  - Print the contents of the file.
  - Close the file.
```python
def confirm_append(file_name):
    """
    Prints the contents of the file to the screen.
    :param file_name: Name of the file (string)
    :return: None
    """
    with open(file_name, 'r') as file:
        print(file.read())
```

**18.3.4) Function: `append_to_ten`**
- Purpose: Initialize a file and appends to  10 lines, then print the contents.
- Parameters: `file_name` (string)
- Returns: None
- Implementation:
  - Use a loop to call `append_file` until the file contains 10 lines.
  - Call `confirm_append` to print the contents of the file.

```python
def append_to_ten(file_name):
    """
    Appends lines to the file until it contains 10 lines, then prints the contents
    :param file_name: Name of the file (string)
    :return: None
    """
    # Initialize
    try:
        with open(file_name, 'x') as new_file:
            pass
    except OSError as ose:
        pass
    # Update
    while True:
        counter = line_counter(file_name)
        if counter >= 10:
            break
        append_file(file_name, counter)
    confirm_append(file_name)
```

**18.4) Call Main Function**
- Ensure the `main` function is called.
```python
if __name__ == "__main__":
    main()
```

#### Submission
- Submit a single source code file named: `file_read.py`.

#### Assessment Criteria
- Correctly implemented and configured functions.
- Proper use of file handling functions to read, append, and confirm file contents.
- Accurate implementation of loop and function calls to manage file content.
- Clear and well-documented code with appropriate comments.

#### 6) Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code to verify that the file handling functions work as expected.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 18
Description: Read and Formatting Data in Files
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

import os


def line_counter(file_name):
    """
    Counts the total number of lines in the specified file
    :param file_name: Name of the file (string)
    :return: Number of lines in the file (integer)
    """
    with open(file_name, 'r') as file:
        counter = sum(1 for line in file)
    return counter


def append_file(file_name, counter):
    """
    Appends a line of text to the file, indicating the updated line count
    :param file_name: Name of the file (string)
    :param counter: Current number of lines in the file (integer)
    :return: None
    """
    with open(file_name, 'a') as file:
        file.write(f"data_file.data had {counter} lines of data, and now it has {counter + 1}\n")


def confirm_append(file_name):
    """
    Prints the contents of the file to the screen
    :param file_name: Name of the file (string)
    :return: None
    """
    with open(file_name, 'r') as file:
        print(file.read())


def append_to_ten(file_name):
    """
    Initializes a file and updates it to contain 10 lines,
    then prints the contents
    :param file_name: Name of the file (string)
    :return: None
    """
    # Initialize
    try:
        with open(file_name, 'x') as new_file:
            pass
    except OSError as ose:
        pass
    # Update
    while True:
        counter = line_counter(file_name)
        if counter >= 10:
            break
        append_file(file_name, counter)
    confirm_append(file_name)


def main():
    print(f'\nWelcome to Lab 18: Read and Format File Data')

    # Prompt user for the filename append to ten
    append_to_ten("format_data.txt")
    return


if __name__ == "__main__":
    main()

```

<hr>
