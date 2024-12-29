### Lab 19: "File IO: Read, Write Byte-Data"

#### Assignment Overview
In this lab, you will extend your work with file management techniques to handle different types of data saved into files.

#### Learning Objectives
- Understand and implement file handling for byte data in Python.
- Use Python's built-in functions to write, read, and decode byte data.
- Practice reading user input and saving it to a file as byte data.

#### Instructions

**19.1) Create File**
- Create a properly formatted Python file named `file_bytes.py` import `os` and `logging`

**19.2) Define Main Function**
- Create and call a function named `main` that takes no data and returns no data.
- Inside the `main` function, create a variable named `file_name = "byte_file.bytes"`, which will act as the name of the file being accessed and manipulated.

**19.3) Define Supporting Functions**
- Define the following functions with appropriate multi-line comments describing their purpose, parameters, and return values:

**19.3.1) Function: `write_bytes`**
- Purpose: Writes a string as byte data to a file.
- Parameters: `file_name` (string), `string_data` (string)
- Returns: None
- Implementation:
  - Use the 'with' file-handling syntax to open the file in 'wb' (write binary) mode.
  - Transform `string_data` into byte data using the built-in `bytes()` function (`bytes(string_data, encoding='utf8')`).
  - Write the byte data to the file.
  - The 'with' file-handling syntax will auto-close the file handle.

```python
def write_bytes(file_name, string_data):
    """
    Writes a string as byte data to a file
    :param file_name: Name of the file (string)
    :param string_data: Data to be written to the file (string)
    :return: None
    """
    try:
        byte_data = bytes(string_data, encoding='utf8')
        if not os.path.exists(file_name):
            with open(file_name, 'wb') as create_file:
                create_file.write(byte_data)
                logging.debug(f" File {file_name} Created")
        else:
            with open(file_name, 'ab') as update_file:
                update_file.write(byte_data)
                logging.debug(f" File {file_name} Updated")
    except OSError as ose:
        logging.warning(f" File Cannot be Created or Updated {ose}")
    return
```

**19.3.2) Function: `print_bytes`**
- Purpose: Reads and prints byte data from a file.
- Parameters: `file_name` (string)
- Returns: None
- Implementation:
  - Use the 'with' file-handling syntax to open the file in 'rb' (read binary) mode.
  - Read the byte data and print it to the screen.

```python
def print_bytes(file_name):
    """
    Reads and prints byte data from file_name
    :param file_name: Name of the file (string)
    :return: None
    """
    with open(file_name, 'rb') as file:
        byte_data = file.read()
        print(f'Read Byte Data Results: \n\t{byte_data}')
    return
```

**19.3.3) Function: `print_strings`**
- Purpose: Reads byte data from a file, decodes it, and prints the resulting string.
- Parameters: `file_name` (string)
- Returns: None
- Implementation:
  - Use the 'with' file-handling syntax to open the file in 'rb' (read binary) mode.
  - Read the byte data.
  - Decode the byte data using `.decode("utf-8")` and print the resulting string.

```python
def print_strings(file_name):
    """
    Reads and decodes byte data from file_name
    and prints the resulting string
    :param file_name: Name of the file (string)
    :return: None
    """
    with open(file_name, 'rb') as file:
        byte_data = file.read()
        # print(f'Temporary Byte Data Found: \n\t{byte_data}')
        string_data = byte_data.decode("utf-8")
        print(f'Read String Data Results: \n\t{string_data}')
        return
```

**19.4) Main Function Implementation**
- Inside the `main` function, prompt the user (using `input()`) to enter a name or a word.
- Use `write_bytes` to save the input as byte data to `file_name`.
- Call both `print_bytes` and `print_strings` to show the data saved in the file to the user.

```python
def main():
    print(f'\nWelcome to Lab 19: Encode/Decode Data in Files')

    # Setup file and prompt user for the data to save
    file_name = "byte_file.bytes"
    print(f'\nThe bytes file is named: {file_name}')
    user_input = input(f'Enter data to save into the file: ')
    write_bytes(file_name, user_input)
    print(f'Byes written to file')
    print(f'{"_ " * 20}')

    print(f'\nByte data in {file_name}:')
    print_bytes(file_name)

    print(f'\nString data in {file_name}:')
    print_strings(file_name)

    return


if __name__ == "__main__":
    main()
```

#### Submission
- Submit a single source code file named: `file_bytes.py`.

#### Assessment Criteria
- Correctly implemented and configured functions.
- Proper use of file handling functions to write, read, and decode byte data.
- Accurate implementation of user input handling and data manipulation.
- Clear and well-documented code with appropriate comments.

#### Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code to verify that the file handling functions work as expected.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 19
Description: Encode/Decode Data in Files
Author: Clinton Garwood
Date: August 2024
License: MIT
"""
import logging
import os


def write_bytes(file_name, string_data):
    """
    Writes a string as byte data to a file
    :param file_name: Name of the file (string)
    :param string_data: Data to be written to the file (string)
    :return: None
    """
    try:
        byte_data = bytes(string_data, encoding='utf8')
        if not os.path.exists(file_name):
            with open(file_name, 'wb') as create_file:
                create_file.write(byte_data)
                logging.debug(f" File {file_name} Created")
        else:
            with open(file_name, 'ab') as update_file:
                update_file.write(byte_data)
                logging.debug(f" File {file_name} Updated")
    except OSError as ose:
        logging.warning(f" File Cannot be Created or Updated {ose}")
    return


def print_bytes(file_name):
    """
    Reads and prints byte data from file_name
    :param file_name: Name of the file (string)
    :return: None
    """
    with open(file_name, 'rb') as file:
        byte_data = file.read()
        print(f'Read Byte Data Results: \n\t{byte_data}')
    return


def print_strings(file_name):
    """
    Reads and decodes byte data from file_name
    and prints the resulting string
    :param file_name: Name of the file (string)
    :return: None
    """
    with open(file_name, 'rb') as file:
        byte_data = file.read()
        # print(f'Temporary Byte Data Found: \n\t{byte_data}')
        string_data = byte_data.decode("utf-8")
        print(f'Read String Data Results: \n\t{string_data}')
        return


def main():
    print(f'\nWelcome to Lab 19: Encode/Decode Data in Files')

    # Setup file and prompt user for the data to save
    file_name = "byte_file.bytes"
    print(f'\nThe bytes file is named: {file_name}')
    user_input = input(f'Enter data to save into the file: ')
    write_bytes(file_name, user_input)
    print(f'Byes written to file')
    print(f'{"_ " * 20}')

    print(f'\nByte data in {file_name}:')
    print_bytes(file_name)

    print(f'\nString data in {file_name}:')
    print_strings(file_name)

    return


if __name__ == "__main__":
    main()

```

<hr>
