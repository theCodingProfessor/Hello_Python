"""
Module Name: Programming Lab 23
Description: FullUser Class, inherits AdminUser override display_data.
Author: Clinton Garwood
Date: August 2024
License: MIT
Classes: FullUser - new user_directory, update last_seen
"""
from AppUser import AppUser
from AdminUser import AdminUser

from enum import Enum


class UserRole(Enum):
    GUEST = "Guest"
    CLIENT = "Client"
    OPERATOR = "Operator"
    ADMIN = "Admin"


class FullUser(AdminUser):
    """
    FullUser extends AdminUser adding user_directory
    Attributes:
        user_directory (str):
    Methods:
        __init__(self, *args, **kwargs): Initializes a new user with a file directory string.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new FullUser: adds user_directory
        Can accept any:
        - AdminUser Objects
        - AppUser, with role and id parameters
        - Keyword values: preferred_name, contact_string, new_role, new_id
        """
        if len(args) == 1 and isinstance(args[0], AdminUser):
            # Handle case where an AdminUser object is passed
            admin_user = args[0]
            super().__init__(admin_user.user_name, admin_user.contact, user_role=admin_user.user_role, user_id=admin_user.user_id)
            if not isinstance(self.user_role, UserRole):
                self.user_role = UserRole[self.user_role.upper()]
            self.user_directory = f'directory_{str(admin_user.user_id)}'
        elif len(args) == 1 and isinstance(args[0], AppUser):
            # Handle case where an AppUser object is passed
            app_user = args[0]
            this_role = kwargs.pop('user_role', 'Guest')
            this_id = kwargs.pop('user_id', -2)
            # print(f'This role and iD {this_role}, {this_id}')
            super().__init__(app_user.user_name, app_user.contact, this_role, this_id)
            if not isinstance(self.user_role, UserRole):
                self.user_role = UserRole[self.user_role.upper()]
            self.user_directory = f'directory_{str(self.user_id)}'
        else:
            # Handle cases where individual strings are passed
            self.user_name = args[0] if len(args) > 0 else 'undefined'
            self.contact = args[1] if len(args) > 1 else 'unknown'
            self.user_role = args[2] if len(args) > 2 else 'Guest'
            self.user_id = args[3] if len(args) > 3 else -2
            super().__init__(self.user_name, self.contact, self.user_role, self.user_id)
            if not isinstance(self.user_role, UserRole):
                self.user_role = UserRole[self.user_role.upper()]
            self.user_directory = f'directory_{str(self.user_id)}'
        self.set_last_seen()  # update last access datetime.datetime.now()

    def set_user_directory(self, new_dir):
        """
        Set the user_id
        :param new_dir: User Directory Name
        :return: None
        """
        self.user_directory = new_dir

    def get_user_directory(self):
        """
        Get the user_directory.
        :return: user_directory (string)
        """
        return self.user_directory

    def display_data(self):
        """
        Updates (overwrites) AppUser format for all data
        :return: None
        """
        # print(f'User Data:')
        # print(f'\tGood Name:\t{self.user_name}')
        # print(f'\tContact:\t{self.contact}')
        # print(f'\tCreated on:\t{self.origin}')
        # print(f'\tUser Name:\t{self.user_name}')
        # print(f'\tUser Role:\t{self.user_role}')
        # print(f'\tUser ID:\t{self.user_id}')
        # print(f'\tMost Recent:\t{self.last_seen}')
        super().display_data()
        print(f'\tDirectory:\t{self.get_user_directory()}')
        return
