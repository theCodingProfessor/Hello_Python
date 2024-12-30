### Lab 21: "External Python Class File"

#### Assignment Overview
In this assignment, you will create a base Python Class in its own file. You will use the `import` statement to connect resources, like the driver you will also create into a working system. The class will include a constructor, getters, setters, and a method to display its data in a formatted manner.

#### Learning Objectives

- Understand the structure and purpose of a Python class.
- Implement class constructors, data members, and methods.
- Use getter and setter methods to manipulate class data members.
- Create and call methods to display class data.

#### Instructions
Explore the concept of an external Class file in OOP Object-Oriented Programming 

**21.1) Create File**
- Create the first (of two) properly formatted Python file named `class_base.py`

**21.2) Define the Class**
- Create a Python class named `AppData` a base class which will be extended. Make sure your data members, constructor and class methods are all indented to the same level. Notice the class constructor, `__init__()`, does take any data. 

```python
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
            contact_string (str): Contact string (e.g., phone or text number, email)
        """
        self.user_name = preferred_name
        self.contact = contact_string
        self.origin = datetime.datetime.now()  # datetime: First access
        self.last_seen = self.origin  # datetime: Most recent access

```

**21.3) Define Setter and Getter Methods**
Create the following setter and getter methods (all equally indented):
```python
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

    def set_contact(self, new_contact):
        """
        Set the user_name
        :param new_contact: (string)
        :return: None
        """
        self.contact = new_contact

    def get_contact(self):
        """
        Get the contact string
        :return: contact
        """
        return self.contact

    def get_origin(self):
        """
        Get the origin datestamp
        :return: origin
        """
        return self.origin

    def get_last_seen(self):
        """
        Get the last_seen datetime object
        :return: last_seen (datetime)
        """
        return self.last_seen

    def set_last_seen(self):
        """
        Update last_seen datetime object
        :return: none
        """
        self.last_seen = datetime.datetime.now()

```

**21.4) Create Driver File:** - Create a properly formatted Python file named `class_base.py`

**21.5) Define Main Function**
1. Create and call a function named `main` that takes no data and returns no data.
2. Inside `main`, create a new object of type `UserData`.
3. Call the setter and getter methods to manipulate and retrieve the object's data members.
4. Call `display_data` to print the formatted data.

```python
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
                new_id = int(input("Enter user ID: "))
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
            user_id = int(input("Enter the user ID to remove: "))
            users = [user for user in users if user.get_user_id() != user_id]
            print("User removed successfully.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

```

#### Submission
Submit two source code files: `class_base.py` `AppUser.py`

#### Assessment Criteria

- Correct implementation of the class with data members, constructor, setter, and getter methods.
- Proper use of class methods to manipulate and display data.
- Accurate implementation of the main function to demonstrate class functionality.
- Clear and well-documented code with appropriate comments.

#### Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code to verify that the class methods work as expected.

<hr>

#### Additional Code
Demonstration Files

- Driver File

```python
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
            name_user = input("Enter the name of the user to remove: ")
            # List comprehension removes object if found
            users = [user for user in users if user.get_user_name() != name_user]
            print("User removed successfully.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

```

- Class File - AppUser.py

```python
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
            contact_string (str): Contact string (e.g., phone or text number, email)
        """
        self.user_name = preferred_name
        self.contact = contact_string
        self.origin = datetime.datetime.now()  # datetime: First access
        self.last_seen = self.origin  # datetime: Most recent access

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

    def set_contact(self, new_contact):
        """
        Set the user_name
        :param new_contact: (string)
        :return: None
        """
        self.contact = new_contact

    def get_contact(self):
        """
        Get the contact string
        :return: contact
        """
        return self.contact

    def get_origin(self):
        """
        Get the origin datestamp
        :return: origin
        """
        return self.origin

    def get_last_seen(self):
        """
        Get the last_seen datetime object
        :return: last_seen (datetime)
        """
        return self.last_seen

    def set_last_seen(self):
        """
        Update last_seen datetime object
        :return: none
        """
        self.last_seen = datetime.datetime.now()

    def display_data(self):
        """
        Presents formatted user data
        :return: None
        """
        print(f'User Data:')
        print(f'\tGood Name:\t{self.user_name}')
        print(f'\tContact:\t{self.contact}')
        print(f'\tCreated on:\t{self.origin}')
        return

```

<hr>
