"""
Module Name: Programming Lab 22
Description: AdminUser Class, inherits AppUser, override display_data.
Author: Clinton Garwood
Date: August 2024
License: MIT
Classes: AdminUser - new user_role, and user_id, update last_seen
"""
from AppUser import AppUser

import datetime


class AdminUser(AppUser):
    """
    AdminUser extends AppUser adding user_role, user_id and a timestamp
    Attributes:
        user_role (str):
        user_id (datetime): Logfile for user directory
    Methods:
        __init__(self, new_name='undefined', new_role='guest', new_id=-1): Initializes a new user with the provided name, role, and ID.
    """
    def __init__(self, new_name='unknown', contact='undefined',
                 user_role='Guest', user_id=-1):
        """
        Initialize a new user already having a name and contact strings.
        New Attributes:
            new_id (int): The unique identifier for the new user.
            new_role (str): The role of the new user.
        """
        # print(f'Admin Constructor start {new_name} {user_id}')
        super().__init__(new_name, contact)
        self.user_role = user_role
        self.user_id = user_id
        self.set_last_seen()  # update last access with datetime.datetime.now()

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
        Updates (overwrites) AppUser format for all data
        :return: None
        """
        super().display_data()
        # print(f'User Data:')
        # print(f'\tGood Name:\t{self.get_user_name()}')
        # print(f'\tContact:\t{self.get_contact()}')
        # print(f'\tCreated on:\t{self.get_origin()}')
        print(f'\tRole:\t{self.get_user_role()}')
        print(f'\tUser ID:\t{self.get_user_id()}')
        print(f'\tMost Recent:\t{self.get_last_seen()}')
        return
