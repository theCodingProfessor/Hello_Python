"""
The Math Calculator
Description: Code Implemented from app_2_design.md
Clinton Garwood
September 2024
License: MIT
ChangeLog: In Data Validation
  see: do_division - all errors are handled in user_prompt
  see: user_prompt
    1) Handle all other conditions from '1 - 4'
        setting float_one = None
        setting float_two = None
    2) Handle all float casting issues by setting static values:
        setting float_one = 0.0
        setting float_two = 1.0
ChangeLog: Changed Exit Message to remove the word `App`
"""


def do_addition(float_one, float_two):
    the_sum = float_one + float_two
    print(f'\n\t\t{float_one} + {float_two} = {the_sum} ')
    return


def do_subtraction(float_one, float_two):
    the_difference = float_one - float_two
    print(f'\n\t\t{float_one} - {float_two} = {the_difference} ')
    return


def do_multiply(float_one, float_two):
    the_product = float_one * float_two
    print(f'\n\t\t{float_one} x {float_two} = {the_product} ')
    return


def do_division(float_one, float_two):
    the_quotient = float_one / float_two
    print(f'\n\t\t{float_one} / {float_two} = {the_quotient} ')
    return


def main_menu():
    print(f'\n\t1) Do Addition')
    print(f'\t2) Do Subtraction')
    print(f'\t3) Do Multiplication')
    print(f'\t4) Do Division')
    print(f'\t5) Exit')
    return


def user_prompt():
    main_menu()
    # Handle Condition of user entering in 5
    menu_option = input(f'\tPlease select an option: ')
    if menu_option in ['1', '2', '3', '4']:
        # Handle Error Conditions
        try:
            float_one = float(input(f"\tEnter the first number: "))
        except ValueError:
            float_one = 0.0
            print(f'\tInvalid Input Received. First Value set to 0')
        try:
            float_two = float(input(f"\tEnter the second number: "))
        except ValueError:
            float_two = 1.0
            print(f'\tInvalid Input Received. Second Value set to 1')
    else:
        float_one = None
        float_two = None
    return menu_option, float_one, float_two


def main():
    print(f'\nWelcome to the Math Calculator')

    # Handle User Interaction
    menu_option, float_one, float_two = user_prompt()
    while menu_option != "5":
        if menu_option == "1":
            do_addition(float_one, float_two)
        elif menu_option == "2":
            do_subtraction(float_one, float_two)
        elif menu_option == "3":
            do_multiply(float_one, float_two)
        elif menu_option == "4":
            do_division(float_one, float_two)
        elif menu_option == "5":
            break
        else:
            print(f'\tInvalid selection. Please try again.')
        menu_option, float_one, float_two = user_prompt()

    print(f'\nThank you for using the Math Calculator')

    return


if __name__ == '__main__':
    main()
