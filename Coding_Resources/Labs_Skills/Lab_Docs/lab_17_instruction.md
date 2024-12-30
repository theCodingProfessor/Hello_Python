### Lab 17: "Try-Except Error Handling for File Management"

#### Assignment Overview
In this lab, you will learn how to catch errors and exceptions and extend your File-IO skills (create, write, append, and read). Additionally, you will use the Path library.

#### Learning Objectives
- Understand how to use try-except (try-catch) blocks for error handling in Python.
- Gain experience with file management operations such as creating, writing, appending, and reading files.
- Learn to use the Path library for file handling.

#### Instructions
**17.1) Create File**
- Create a properly formatted Python file named `try_except.py` imports `os` and `logger` 

```python
"""
Module Name: Programming Lab 17
Description: Try-Catch Handling and Path Library
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

import os

# Reuse `logger` from a previous module
import lab_15_module as logger_lab
logger = logger_lab.create_default_logger()

def main():
    print(f'\nWelcome to Lab 17: Try-Catch and Path Library')
    logger.debug(f"logger is available.")

    # Review the scope of imports and logger initialization
    name_string = input(f'\tProvide a name for a file or directory: ')

    # Create and Remove Coding_Resources (Files)
    os_file_handling(name_string)

    # Create and Remove Coding_Resources (Directories)
    path_file_handling(name_string)

    # Introduce Try-Catch Feature
    try_catch(name_string)

    return

if __name__ == "__main__":
    main()
```

**17.2) Implement `try_catch` Function**
- Define a function `try_catch` that takes a string `resource_name_string`.
- Use try-catch blocks to handle errors and exceptions for both files and directories.
```python
def try_catch(resource_name_string):
    """
    Handle exceptions using Python try-except block.
    The best practice is to catch specific exceptions rather
    than using a broad OSError (both methods shown below).
    :param resource_name_string:
    :return:
    """
    print(f'\nInside try_catch: \n\tCurrent Directory: {os.getcwd()}')

    # Try-Catch using broad OSError when on a file
    try:
        with open(resource_name_string, 'r') as open_resource:
            print(f'{open_resource.read()}')
    except OSError as os_error:
        logger.warning(f"{os_error}")

    # Attempt to navigate to a directory of that name
    try:
        os.chdir(resource_name_string)
        print(f'\tSuccessfully navigated to {resource_name_string}')
    except FileNotFoundError:
        print(f'\tError: The directory "{resource_name_string}" does not exist.')
    except PermissionError:
        print(f'\tError: Insufficient permissions to access "{resource_name_string}".')
    except NotADirectoryError:
        print(f'\tError: "{resource_name_string}" is not a directory.')
    except OSError as e:
        # Catch any other OSError that may occur
        print(f'\tError: {e}')
    return
```

**17.3) Implement `path_file_handling` Function**
- Define a function `path_file_handling` that takes a string `file_name_string`.
- Use the Path library to handle file creation and modification.
```python
def path_file_handling(file_name_string):
    print(f'\nInside path_file_handling: \n\tCurrent Directory: {os.getcwd()}')

    # Path import and object implementation
    from pathlib import Path
    file_path = Path(file_name_string)

    # Check if file_path is valid (exists as a resource or directory)
    #   use with object.open() syntax (method of Path)
    if file_path.exists():
        with file_path.open('a') as f:
            logger.debug(f"File Update Succeeded")
            f.write(f'\nAppended Data using Path library')
    else:
        with file_path.open('w') as f:
            f.write(f'Created file named {file_name_string}')
            logger.debug(f"File Creation Succeeded")
    return
```

**17.4) Implement `os_file_handling` Function**
- Define a function `os_file_handling` that takes a string `file_name_string`.
- Use the `os` module to handle file creation and modification.
```python
def os_file_handling(file_name_string):
    # `os` is already in scope (outer) usage
    print(f'\nInside os_file_handling: \n\tCurrent Directory: {os.getcwd()}')

    # Check if file_path is valid (exists as a resource or directory)
    #   and use with open(file, mode) as file_handle: syntax 
    if os.path.exists(file_name_string):
        with open(file_name_string, 'a') as f:
            f.write(f'\nAppended Data using os library')
            logger.debug(f"File Update Succeeded")
    else:
        with open(file_name_string, 'w') as f:
            f.write(f'Created Resource {file_name_string}')
            logger.debug(f"File Creation Succeeded")
    return
```

#### Submission
- Submit a single source code file named: `try_catch.py`.

#### Assessment Criteria
- Correctly implemented and configured functions.
- Proper use of try-catch blocks for error handling.
- Accurate implementation of file management using both `os` and Path libraries.
- Clear and well-documented code with appropriate comments.

#### 6) Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code to verify that the try-catch blocks and file management functions work as expected.
- Refer to the official Python documentation for additional details and examples on try-catch blocks and the Path library.

<hr>

Additional Topics: 


- 
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
Module Name: Programming Lab 17
Description: Try-Catch Handling and Path Library
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

import os

# Reuse `logger` from a previous module
from apps.docs.python_exercises import lab_15_code as logger_lab

logger = logger_lab.create_default_logger()


# Programmatic implementation of a logger
# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)


def os_file_handling(file_name_string):
    # `os` is already in scope (outer) usage
    print(f'\nInside os_file_handling: \n\tCurrent Directory: {os.getcwd()}')

    # Check if file_path is valid (exists as a resource or directory)
    #   and use with open(file, mode) as file_handle: syntax
    if os.path.exists(file_name_string):
        with open(file_name_string, 'a') as f:
            f.write(f'\nAppended Data using os library')
            logger.debug(f"File Update Succeeded")
    else:
        with open(file_name_string, 'w') as f:
            f.write(f'Created Resource {file_name_string}')
            logger.debug(f"File Creation Succeeded")
    return


def path_file_handling(file_name_string):
    print(f'\nInside path_file_handling: \n\tCurrent Directory: {os.getcwd()}')

    # Path import and object implementation
    from pathlib import Path
    file_path = Path(file_name_string)

    # Check if file_path is valid (exists as a resource or directory)
    #   use with object.open() syntax (method of Path)
    if file_path.exists():
        with file_path.open('a') as f:
            logger.debug(f"File Update Succeeded")
            f.write(f'\nAppended Data using Path library')
    else:
        with file_path.open('w') as f:
            f.write(f'Created file named {file_name_string}')
            logger.debug(f"File Creation Succeeded")
    return


def try_catch(resource_name_string):
    """
    Handle exceptions using Python try-except block.
    The best practice to catch specific exceptions rather
    than using a broad OSError (both methods shown below)
    :param resource_name_string:
    :return:
    """
    print(f'\nInside try_catch: \n\tCurrent Directory: {os.getcwd()}')

    # Try-Catch using broad OSError when on a file
    try:
        with open(resource_name_string, 'r') as open_resource:
            print(f'{open_resource.read()}')
    except OSError as os_error:
        logger.warning(f"{os_error}")

    # Attempt to navigate a directory of that name
    # Attempt to navigate to a directory of that name
    try:
        os.chdir(resource_name_string)
        print(f'\tSuccessfully navigated to {resource_name_string}')
    except FileNotFoundError:
        print(f'\tError: The directory "{resource_name_string}" does not exist.')
    except PermissionError:
        print(f'\tError: Insufficient permissions to access "{resource_name_string}".')
    except NotADirectoryError:
        print(f'\tError: "{resource_name_string}" is not a directory.')
    except OSError as e:
        # Catch any other OSError that may occur
        print(f'\tError: {e}')
    return


def main():
    print(f'\nWelcome to Lab 17: Try-Catch and Path Library')

    # Review the scope of imports and logger initialization
    name_string = input(f'\tProvide a name for a file or directory: ')

    # Create and Remove Coding_Resources (Files)
    os_file_handling(name_string)

    # Create and Remove Coding_Resources (Directories)
    path_file_handling(name_string)

    # Introduce Try-Catch Feature
    try_catch(name_string)

    return


if __name__ == "__main__":
    main()

```

<hr>
