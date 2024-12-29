"""
Module Name: Programming Lab 21
Description: External Class File and Python Driver
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

from AppUser import AppUser


def main():
    print(f'\nWelcome to Lab 21: Python Inheritance (Parent, Child)')

    users = []
    while True:
        print("\n1. Create a new user")
        print("2. View all users")
        print("3. Remove a user")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                new_name = input("Enter user name: ")
                new_role = input("Enter user role: ")
                user = AppUser(new_name, new_role)
                users.append(user)
                print("User created successfully.")
            except ValueError:
                print("Invalid input. Please enter valid data.")

        elif choice == '2':
            if users:
                for user in users:
                    user.display_data()
            else:
                print("No users available.")

        elif choice == '3':
            name_user = input("Enter the Username to remove: ")
            # List comprehension removes object if found
            users = [user for user in users if user.get_user_name() != name_user]
            print("User removed successfully.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
