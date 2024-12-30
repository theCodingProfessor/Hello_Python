"""
Module Name: Programming Lab 21
Description: AppUser data: user_name, contact, creation timestamp
Author: Clinton Garwood
Date: August 2024
License: MIT
Classes: AppUser - Parent Class Method: display_data()
"""
import datetime


class AppUser:
    """
    A class to represent an application user.
    Attributes:
        user_name (str): The name of the user.
        contact (str): A contact string for the user.
        origin (datetime): The unique identifier for the user.
        last_seen (datetime): Most recent timestamp
    Methods:
        __init__(self, new_name='unknown', contact_at='undefined')
    """

    def __init__(self, preferred_name='unknown', contact_string='undefined'):
        """
        Initialize Users Name and Contact Information
        Parameters:
            preferred_name (str): The name of the new user.
            contact_string (str): Contact string (for example, phone or text number, email)
        """
        self.user_name = preferred_name
        self.contact = contact_string
        self.origin = datetime.datetime.now()  # datetime: First access
        self.last_seen = self.origin  # datetime: Most recent access

    def set_user_name(self, name):
        """
        Set the user_name
        :param name: Username (string)
        :return None:
        """
        self.user_name = name

    def get_user_name(self):
        """
        Get the user_name
        :return user_name: Username (string)
        """
        return self.user_name

    def set_contact(self, new_contact):
        """
        Set the user_name
        :param new_contact: (string)
        :return:
        """
        self.contact = new_contact

    def get_contact(self):
        """
        Get the contact string
        :return contact:
        """
        return self.contact

    def get_origin(self):
        """
        Get the origin datestamp
        :return origin:
        """
        return self.origin

    def get_last_seen(self):
        """
        Get the last_seen datetime object
        :return last_seen: A datetime object
        """
        return self.last_seen

    def set_last_seen(self):
        """
        Update last_seen datetime object
        :return:
        """
        self.last_seen = datetime.datetime.now()

    def display_data(self):
        """
        Presents formatted user data
        :return:
        """
        print(f'User Data:')
        print(f'\tGood Name:\t{self.user_name}')
        print(f'\tContact:\t{self.contact}')
        print(f'\tCreated on:\t{self.origin}')
        return
