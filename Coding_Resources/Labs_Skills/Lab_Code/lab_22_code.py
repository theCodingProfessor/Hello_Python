"""
Module Name: Programming Lab 22
Description: Multiple Class Inheritance, Overridden Methods
filename: object_inherit.py
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

from AppUser import AppUser
from AdminUser import AdminUser


def main():
    print(f'\nWelcome to Lab 22: Simple Class Inheritance, Overridden Methods')

    while True:
        print(f"\n\t1. Create AppUser")
        print(f"\t2. Create AdminUser")
        print(f"\t3. Exit")
        choice = input(f"\tPlease select: ")

        if choice == '1':  # Create AppUser
            try:
                new_name = input(f"\n\tPreferred Name: ")
                new_contact = input(f"\tContact Data: ")
                if new_name == '' or new_contact == '':
                    user = AppUser()
                else:
                    user = AppUser(new_name, new_contact)
                print()
                user.display_data()  # uses parent method
            except ValueError:
                print(f"\n\tSorry, improper input. Please try again.")

        elif choice == '2':  # Create AdminUser
            try:
                new_name = input(f"\n\tPreferred Name: ")
                new_contact = input(f"\tContact Data: ")
                new_role = input(f"\tRole: \n\tDefault=Guest. Others are Client, Operator, Admin: ")
                try:
                    new_id = int(input(f"\tUser Number: "))
                except ValueError:
                    new_id = None
                a_user = AdminUser(new_name, new_contact)
                b_user = AdminUser(new_name, new_contact, new_role)
                c_user = AdminUser(new_name, new_contact, new_role, new_id)
                a_user.display_data()  # uses child overridden method
                b_user.display_data()  # uses child overridden method
                c_user.display_data()  # uses child overridden method
            except Exception as any_exception:
                print(f"\n\tThis happened {any_exception}")

        elif choice == '3':
            break

        else:
            print(f"\n\tPlease try again.")


if __name__ == "__main__":
    main()
