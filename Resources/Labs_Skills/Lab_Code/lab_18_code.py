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
