"""
Module Name: Programming Lab 16
Description: Operating System Libraries
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def os_navigate_features():
    # Get the current working directory
    print(f'\nInside os_navigate')
    print(f'\tCurrent directory: {os.getcwd()}')

    # Display any resources found in working directory
    print(f'\tResources Found: {os.listdir()}')

    return


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
            os.chdir("../../code_demos")
            os.rmdir(new_dir_name)
            print(f'\t\tDirectory {new_dir_name} removed.')
        else:
            os.chdir("../../code_demos")
            print(f'\t\tDirectory {new_dir_name} is now available.')
    else:
        print(f'\t\tDirectory {new_dir_name} already exists.')
    return


def os_file_features():
    print(f'\nInside os_file_features')
    print(f'\tInitial Resources: {os.listdir()}')

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
    print(f'\n\tIn this location: {os.getcwd()}')
    print(f'\tResources Found: {os.listdir()}')

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
    import os
    main()
