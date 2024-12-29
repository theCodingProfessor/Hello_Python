"""
Module Name: Programming Lab 11
Description: Higher-Order Functions: Passing Functions as Parameters
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def multiverse_0(visitor):
    """
    Function takes a string and passes the string back to the caller
    :param: visitor str
    :return: visitor
    """
    return visitor


def multiverse_1(visitor):
    """
    Takes a string, concatenates it and passes it back to the caller
    :param: visitor str
    :return: string
    """
    return f'{visitor} from Multiverse 1'


def multiverse_2(visitor):
    """
    Takes a string and passes only a message back to the caller
    :param: visitor str
    :return: string
    """
    return f'There is no escape from Multiverse 2'


def main():
    """
    The main function is the driver that runs the program.
    """
    print(f'\nWelcome to Lab 11: Passing a Function as a Parameter.')

    # Prompt the user for data and report it back to the user
    user_name = input('Please enter your preferred name: ')
    print(f'\nYou entered: {user_name}')

    # Call each function giving it the value received from the user
    print(f'\nSimple Function Callers >> Values')
    print(f'\tmultiverse_0({user_name}) returns >> {multiverse_0(user_name)}')
    print(f'\tmultiverse_1({user_name}) >> {multiverse_1(user_name)}')
    print(f'\tmultiverse_2({user_name}) >> {multiverse_2(user_name)}')

    # Make nested function calls (higher-level functions)
    print(f'\nNested Function Callers >> Values')
    print(f'\tmultiverse_0(multiverse_1({user_name})) >> {multiverse_0(multiverse_1(user_name))}')
    print(f'\tmultiverse_0(multiverse_2({user_name})) >> {multiverse_0(multiverse_2(user_name))}')
    print(f'\tmultiverse_0(multiverse_1(multiverse_2({user_name}))) >> {multiverse_0(multiverse_1(multiverse_2(user_name)))}')

    return


main()
