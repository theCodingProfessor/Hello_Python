"""
Module Name: Programming Lab 10
Description: Functions as Reusable/Callable Code
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def just_print():
    print(f'\tInside the just_print function.')
    return


def add_and_return(number_in):
    return number_in + number_in


def empty_or_not(string_in):
    """
    This function takes a string variable and
    checks it to determine if it is an empty string or not.
    If the string has data (is valid), the variable status
    is updated to true (or 1). The value of status (updated or not)
    is returned to the caller.
    """
    status = 0
    if len(string_in) > 0:
        status = 1
    return status


def main():
    print(f'\nWelcome to Lab 10: Functions as Reusable Code.')

    # Call just_print() does not take or return data
    print(f'\nNow calling just_print()')
    just_print()

    # Call add_and_return(int) takes and returns integer
    # Be sure to catch the returned value.
    print(f'\nNow calling add_and_return(int)')
    catch_twenty = add_and_return(10)
    print(f'\tadd_and_return(10) returned {catch_twenty}')

    # Call empty_or_not(valid_string)
    # Be sure to catch the returned value.
    print(f'\nNow calling empty_or_not(string)')
    catch_one = empty_or_not('all good')
    print(f'\tempty_or_not("all good") returns {catch_one}')

    return


main()
