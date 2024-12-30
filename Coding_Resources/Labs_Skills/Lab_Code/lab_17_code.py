"""
Module Name: Programming Lab 17
Description: Try-Catch Handling and Path Library
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


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
    import os

    # Reuse `logger` from a previous module
    import lab_15_code as logger_lab
    logger = logger_lab.create_stream_logger()

    # Programmatic implementation of a logger
    # import logging
    # logger = logging.getLogger()
    # logger.setLevel(logging.DEBUG)
    main()
