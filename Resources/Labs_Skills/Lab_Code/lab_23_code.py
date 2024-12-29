"""
Module Name: Programming Lab 23
Description: Polymorphism and Overloaded Object Constructor
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

from AppUser import AppUser
from AdminUser import AdminUser
from FullUser import UserRole, FullUser


def main():
    print(f'\nWelcome to Lab 23: Polymorphism and Overloaded Object Constructor')

    user_pool = []
    # valid_users = []
    while True:
        print("\n1. Create AppUser")
        print("2. Create AdminUser")
        print("3. Create FullUser with AppUser, AdminUser object")
        print("4. Create FullUser without starter object(s)")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':  # Create AppUser
            try:
                new_name = input("Preferred Name: ")
                new_contact = input("Contact Data: ")
                app_user = AppUser(new_name, new_contact)
                print("AppUser object created.")
                app_user.display_data()  # uses parent method
                user_pool.append(app_user)
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '2':  # Create AdminUser
            try:
                new_name = input("Preferred Name: ")
                new_contact = input("Contact Data: ")
                new_role = input("Role: \n\tDefault=Guest, Client, Operator or Admin: ")
                new_id = int(input("User Number: "))
                admin_user = AdminUser(new_name, new_contact, new_role, new_id)
                print("AdminUser object created.")
                admin_user.display_data()  # uses child overridden function
                user_pool.append(admin_user)
            except Exception as any_exception:
                print(f"This happened {any_exception}")

        elif choice == '3':
            for each, user in user_pool:
                if isinstance(user, AppUser) and not isinstance(user, AdminUser):
                    new_role = input("User Role: \n\tGuest, Client, Admin")
                    new_id = int(input("User Number: "))
                    full_user = FullUser(user.user_name, user.contact, new_role, new_id)
                    print("FullUser(AppUser) object created.")
                    full_user.display_data()  # uses overridden function
                    user_pool.pop(each)
                if isinstance(user, AdminUser) and not isinstance(user, AppUser):
                    full_user = FullUser(user.user_name, user.contact, user.user_role, user.user_id)
                    print("FullUser(AdminUser) object created.")
                    full_user.display_data()  # uses overridden function
                    user_pool.pop(each)

        if choice == '4':  # Create FullUser Direct Input
            try:
                new_name = input("Preferred Name: ")
                new_contact = input("Contact Data: ")
                new_role = input("User Role: \n\tGuest, Client, Admin")
                new_id = int(input("User Number: "))
                full_user = FullUser(user_name=new_name, contact=new_contact, user_role=new_role, user_id=new_id)
                print("FullUser object created.")
                full_user.display_data()  # uses overridden function
            except ValueError:
                print("Invalid input. Please enter valid data.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")
    return


if __name__ == "__main__":
    main()
