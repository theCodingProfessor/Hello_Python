### Lab 16: "Python Libraries (i.e., os)"

#### Assignment Overview
In this lab, you will extend your work with built-in Python libraries by using the `os` library to navigate, create, and remove resources in an environment. Additionally, you will be introduced to simple file creation using the `open()` syntax.

#### Learning Objectives
- Understand how to use the `os` library for file system navigation.
- Learn to create and remove directories using the `os` library.
- Gain skills in creating and modifying files using the `open()` function.

#### Instructions
**16.1) Create File**
- Create a properly formatted Python file named `operating_system.py` use `import os`

**16.2) Define Stub Functions and Main Function**
- Start by creating three stub functions: `os_navigate_features`, `os_directory_features`, and `os_file_features`.
- Define a `main` function that will call these stub functions:
```python
def main():
    print(f'\nWelcome to Lab 16: Python Libraries (i.e., `os`)')

    # Review the timing (scope) for where to use the statement
    # import os

    # Use `os` features exposed by user defined functions

    # Handle File System Navigation
    os_navigate_features()

    # Create and Remove Coding_Resources (Directories)
    os_directory_features()

    # Create and Remove Coding_Resources (Files)
    os_file_features()

    return

main()
```

**3.3) Implement `os_navigate_features` Function**
Use `os.getcwd()` to discover and report the current directory.
Use `os.listdir()` to print the names of any files or other directories in the current directory.
```python
def os_navigate_features():
    # Get the current working directory
    print(f'\nInside os_navigate_features')
    print(f'\tCurrent directory: {os.getcwd()}')

    # Display any resources found in the working directory
    print(f'\tCoding_Resources Found: {os.listdir(".")}')

    return
```

**3.4) Implement `os_directory_features` Function**
- Report the current directory using `os.getcwd()`.
- Prompt the user for a new directory name. If the directory doesn't exist, create it; otherwise, report that it already exists.
- If newly created, offer the user an option to remove the directory before returning.
```python
def os_directory_features():
    print(f'\nInside os_directory_features')
    print(f'\tCurrent directory: {os.getcwd()}')
    new_dir_name = input(f'\tName for the new directory? ')
    if not os.path.isdir(new_dir_name):
        os.mkdir(new_dir_name)

        # Change into the new directory and report location
        os.chdir(new_dir_name)
        print(f'\tInside {new_dir_name} as path: {os.getcwd()}')

        remove_dir = input(f'\tEnter "1" to maintain this directory: ')
        if remove_dir != '1':
            os.chdir("..")
            os.rmdir(new_dir_name)
            print(f'\t\tDirectory {new_dir_name} removed.')
        else:
            os.chdir("..")
            print(f'\t\tDirectory {new_dir_name} is now available.')
    else:
        print(f'\t\tDirectory {new_dir_name} already exists.')
    return
```

**3.5) Implement `os_file_features` Function**
- Define a string filename and create a new file if it doesn't already exist using `open()` syntax.
- If the file already exists, update the file using `open('a')` mode.
```python
def os_file_features():
    print(f'\nInside os_file_features')
    print(f'\tInitial Coding_Resources: {os.listdir(".")}')

    # Create a new file in the directory
    filename = "test_file.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(f'Created this file named {filename}.')
            print(f'\t\tNew file created and written to.')
    else:
        with open(filename, 'a') as f:
            f.write(f'\nInsert a line of text into the file.')
            print(f'\t\tExisting file appended.')

    # List files in the current directory
    print(f'\tIn this location: {os.getcwd()}')
    print(f'\tCoding_Resources Found: {os.listdir(".")}')

    # Optional: Remove the file
    # os.remove(filename)
    return
```

#### Submission
- Submit a single source code file named: `operating_system.py`.

#### Assessment Criteria
- Correctly implemented and configured functions.
- Proper use of the `os` library for file system navigation, directory creation/removal, and file creation/modification.
- Accurate implementation of the main function and its calls to the defined functions.
- Clear and well-documented code with appropriate comments.

#### 6) Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code to verify that the `os` library functions work as expected.
- Refer to the official Python `os` library documentation for additional details and examples.


<hr>

Additional Topics: 

[Python `os` Library Documentation](https://docs.python.org/3/library/os.html)
**`os`**:
   - **Purpose**: Provides a way of using operating system-dependent functionality like reading or writing to the file system, interacting with environment variables, and handling file and directory operations.
   - **Common Functions**:
     - `os.listdir()`: Lists the files and directories in a specified path.
     - `os.path.join()`: Joins one or more path parts intelligently.
     - `os.getenv()`: Retrieves the value of an environment variable.

   ```python
import os

print(os.listdir())
   ```


- Path Library Function
```python
def path_library():
    from pathlib import Path

    file_path = Path('test_file.txt')

    if not file_path.exists():
        with file_path.open('w') as f:
            f.write('Hello, world!')
    return
```


- Unit Testing Function
```python
def unit_testing():
    """
    Provides a truth-table type test suite for os_functions
    Learn more about these libraries
    import unittest
    import pytest
    import doctest
    :return:
    """
    # os_functions(False, False, False, log_object)
    # os_functions(False, False, True, log_object)
    # os_functions(False, True, False, log_object)
    # os_functions(False, True, True, log_object)
    # os_functions(True, False, False, log_object)
    # os_functions(True, False, True, log_object)
    # os_functions(True, True, False, log_object)
    # os_functions(True, True, True, log_object)
    return
```

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 16
Description: Operating System Libraries
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

import os

def os_navigate_features():
    # Get the current working directory
    print(f'\nInside os_navigate')
    print(f'\tCurrent directory: {os.getcwd()}')

    # Display any resources found in working directory
    print(f'\tCoding_Resources Found: {os.listdir(".")}')

    return


def os_directory_features():
    print(f'\nInside os_create_directory')
    print(f'\tCurrent directory: {os.getcwd()}')
    new_dir_name = input(f'\tName for the new directory? ')
    if not os.path.isdir(new_dir_name):
        os.mkdir(new_dir_name)

        # Change into the new directory and report location
        os.chdir(new_dir_name)
        print(f'\tInside {new_dir_name} as path: {os.getcwd()}')

        remove_dir = input(f'\tEnter "1" to maintain this directory: ')
        if remove_dir != '1':
            os.chdir("..")
            os.rmdir(new_dir_name)
            print(f'\t\tDirectory {new_dir_name} removed.')
        else:
            os.chdir("..")
            print(f'\t\tDirectory {new_dir_name} is now available.')
    else:
        print(f'\t\tDirectory {new_dir_name} already exists.')
    return


def os_file_features():
    print(f'\nInside os_create_file')
    print(f'\tInitial Coding_Resources: {os.listdir(".")}')

    # Create a new file in the directory
    filename = "test_file.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(f'Created this file named {filename}.')
            print(f'\t\tNew file created and written to.')
    else:
        with open(filename, 'a') as f:
            f.write(f'\nInsert a line of text into the file.')
            print(f'\t\tExisting file appended.')

    # List files in the current directory
    print(f'\tIn this location: {os.getcwd()}')
    print(f'\tCoding_Resources Found: {os.listdir(".")}')

    # Optional Remove the file
    # os.remove(filename)
    return


def main():
    print(f'\nWelcome to Lab 16: Python Libraries (i.e., `os`)')

    # Review the timing (scope) for where to use the statement
    # import os

    # Use `os` features exposed by user defined functions

    # Handle File System Navigation
    os_navigate_features()

    # Create and Remove Coding_Resources (Directories)
    os_directory_features()

    # Create and Remove Coding_Resources (Files)
    os_file_features()

    return


if __name__ == "__main__":
    main()

```

<hr>
