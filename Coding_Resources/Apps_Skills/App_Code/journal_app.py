"""
The Journal App
Description: Code Implemented from app_3_design.md
Clinton Garwood
November 2024
License: MIT
ChangeLog: Function get_journal_choice didn't have a prompt string provided.
ChangeLog: Function add_entry didn't have a prompt string provided.
ChangeLog: Updated add_entry write to file to bring date to front.
ChangeLog: line_count added as variable for most_recent(journal_file_name, line_count)
ChangeLog: All files access records datetime stamp at the beginning of its line
"""
import os
import datetime


def configure_file(string_file_name):
    """
    This file sets up the text file for the application
    :param string_file_name:
    :return:
    """
    if not os.path.exists(string_file_name):
        with open(string_file_name, 'w') as write_file:
            write_file.write(f'{str(datetime.datetime.now())} :: This file {string_file_name} created.\n')
        print(f"New file created and written to.")
    else:
        with open(string_file_name, 'a') as update_file:
            update_file.write(f'{str(datetime.datetime.now())} :: Journal Access\n')
        print(f"{string_file_name} was updated.")
    return


def journal_menu():
    print(f'\n\t1) Add Entry')
    print(f'\t2) Read Most Recent Entry')
    print(f'\t3) Read All Entries')
    print(f'\t4) Exit')
    pass


def get_journal_choice():
    user_choice = input(f"\tPlease Select an Entry: ")
    return user_choice


def add_entry(string_file_name):
    """
    Prompts a user for string data to save to file
    :param string_file_name:
    :return:
    """
    new_entry = input(f"\tPlease Enter New Entry: ")
    if not os.path.exists(string_file_name):
        with open(string_file_name, 'w') as write_file:
            write_file.write(f'{str(datetime.datetime.now())} :: This file {string_file_name} created.\n')
            write_file.write(f"Added: {str(datetime.datetime.now())} :: {new_entry}\n")
        print(f"\tNew file created and written to.")
    else:
        with open(string_file_name, 'a') as update_file:
            update_file.write(f"{str(datetime.datetime.now())} :: Added {new_entry}\n")
        print(f"\tFile updated.")
    pass


def most_recent(string_file_name, integer_lines):
    """
    Read and print the number `integer_lines` to the screen
    :param string_file_name:
    :param integer_lines:
    :return:
    """
    lines = []
    if os.path.exists(string_file_name):
        with open(string_file_name, 'r') as read_file:
            for line in range(integer_lines):
                line = read_file.readline()
                if not line:  # Stop if we reach the end of the file
                    break
                lines.append(line.strip())
        for each in lines:
            print(f'\t{each}')
        with open(string_file_name, 'a') as update_file:
            update_file.write(f'{str(datetime.datetime.now())} :: Read Access Partial\n')
        print(f"\t{string_file_name} was updated.")
    pass


def read_all(string_file_name):
    """
    Read and print all the lines in the file to the screen
    :param string_file_name:
    :return:
    """
    if os.path.exists(string_file_name):
        print(f"\nFull Journal:")
        with open(string_file_name, 'r') as read_file:
            print(read_file.read())
            # not formatted well
        with open(string_file_name, 'a') as update_file:
            update_file.write(f'{str(datetime.datetime.now())} :: Read Access Full\n')
        print(f"\t{string_file_name} was updated.")
    pass


def main():
    print(f'\nWelcome to the Personal Journal App.')

    result, line_count = 0, 5
    journal_file_name = 'the_journal.txt'
    configure_file(journal_file_name)

    while True:
        journal_menu()
        user_choice = get_journal_choice()
        if user_choice == '1':
            add_entry(journal_file_name)
        elif user_choice == '2':
            most_recent(journal_file_name, line_count)
        elif user_choice == '3':
            read_all(journal_file_name)
        elif user_choice == '4':
            print(f'Exiting...')
            break
        else:
            print(f"Invalid choice. Please select again.")

    print(f'\nA Journal Links Your Goals to your Data.')

    return


if __name__ == '__main__':
    main()
