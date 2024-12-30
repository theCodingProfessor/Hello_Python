"""
Module Name: Programming Lab 20
Description: Simple Python Class File
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


class UserData:
    user_name, user_role, user_id = "undefined", "guest", -1

    def __init__(self):
        print(f'\nUserData Constructor Called')

    def set_user_name(self, name):
        """
        Set the user_name
        :param name: User name (string)
        :return: None
        """
        self.user_name = name

    def get_user_name(self):
        """
        Get the user_name
        :return: User name (string)
        """
        return self.user_name

    def set_user_role(self, role):
        """
        Set the user_role
        :param role: User role (string)
        :return: None
        """
        self.user_role = role

    def get_user_role(self):
        """
        Get the user_role
        :return: User role (string)
        """
        return self.user_role

    def set_user_id(self, new_id):
        """
        Set the user_id
        :param new_id: User ID (int)
        :return: None
        """
        self.user_id = new_id

    def get_user_id(self):
        """
        Get the user_id.
        :return: User ID (int)
        """
        return self.user_id

    def display_data(self):
        """
        Presents formatted user data
        :return: None
        """
        print(f'User Data:')
        print(f'\tUser Name: {self.user_name}')
        print(f'\tUser Role: {self.user_role}')
        print(f'\tUser ID: {self.user_id}')
        return


def main():
    print(f'\nWelcome to Lab 20: Class Files and Objects')

    user = UserData()

    user.set_user_name("Alice")
    print(f'\t{user.get_user_name()}')

    user.set_user_role("Admin")
    print(f'\t{user.get_user_role()}')

    user.set_user_id(12345)
    print(f'\t{user.get_user_id()}')

    user.display_data()
    return


if __name__ == "__main__":
    main()
