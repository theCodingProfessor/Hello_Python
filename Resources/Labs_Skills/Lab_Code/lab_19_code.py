"""
Module Name: Programming Lab 19
Description: Encode/Decode Data in Files
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

import os
import logging


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
        else:
            with open(file_name, 'ab') as update_file:
                update_file.write(byte_data)
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
