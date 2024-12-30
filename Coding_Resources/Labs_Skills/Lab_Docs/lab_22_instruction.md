### Lab 22: "Object Inheritance and Multiple Classes"

#### Assignment Overview
In this assignment, you will extend your skills in object-oriented programming by creating a new class `AdminUser` that inherits from `AppUser`. This will help you understand parent and child (inheritance) object relationships. The `AdminUser` class will add new data members and override the display method to include additional information.

#### Learning Objectives
- Implement class inheritance in Python.
- Understand the relationship between parent and child classes.
- Add and manage additional data members in derived classes.
- Override methods in derived classes to enhance functionality.

#### Instructions
Explore a Class and how to create objects from that resource. 

**22.1) Create File:** - Create a properly formatted Python file named `AdminUser.py`
1. Use object inheritance to define `AdminUser` as a child class of `AppUser` (the base class from previous labs).
2. Add two data members to `AdminUser`: `user_role` (string) and `user_id` (integer).
3. Create getter and setter methods for these two data members.
4. Override the `display_data` method to present all data members of `AdminUser`.
5. The `AdminUser` class constructor should take two arguments and call the `super()` method of its parent class, passing in the necessary data for those variables.
6. Ensure the `AdminUser` class updates the `last_seen` attribute.

Example `AdminUser` class:
```python
from AppUser import AppUser

import datetime


class AdminUser(AppUser):
    """
    AdminUser extends AppUser adding user_role and user_id
    Attributes:
        user_role (str): .
        user_id (datetime): Logfile for user directory
    Methods:
        __init__(self, new_name='undefined', new_role='guest', new_id=-1): Initializes a new user with the provided name, role, and ID.
    """
    def __init__(self, new_name='unknown', contact='undefined', user_role='Guest', user_id=-1):
        """
        Initializes a new user with the provided name, role, and ID.
        Parameters:
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

```

**22.2) Create File:** 
1. Create the second (of two) properly configured Python file named `object_inherit.py`
2. At the top of the file, include the `AppUser` class.
3. Define and call a `main()` function that takes no data and returns no data.
4. Implement a menu loop that allows the user to:
   - Create `AppUser`
   - Create `AdminUser`
5. For each option, prompt the user for data (or use static values) to create the object, and use the `display_data` function to display the object's data.
6. Test the script by running `object_inherit.py` and creating new objects of each type to ensure the inheritance feature works correctly.

Example `main()` function:

```python
from AppUser import AppUser
from apps.docs.python_exercises.labs.versions.code.AdminUser import AdminUser


def main():
   print(f'\nWelcome to Lab 22: Multiple Class Inheritance, Overridden Methods')

   while True:
      print("\n1. Create AppUser")
      print("2. Create AdminUser")
      print("3. Exit")
      choice = input("Enter your choice: ")

      if choice == '1':  # Create AppUser
         try:
            new_name = input("Preferred Name: ")
            new_contact = input("Contact Data: ")
            user = AppUser(new_name, new_contact)
            user.display_data()  # uses parent method
         except ValueError:
            print("Invalid input. Please enter valid data.")

      elif choice == '2':  # Create AdminUser
         try:
            new_name = input("Preferred Name: ")
            new_contact = input("Contact Data: ")
            new_role = input("Role: \n\tDefault=Guest, Client, Operator or Admin: ")
            new_id = int(input("User Number: "))
            admin_user = AdminUser(new_name, new_contact, new_role, new_id)
            admin_user.display_data()  # uses child overridden function
         except Exception as any_exception:
            print(f"This happened {any_exception}")

      elif choice == '3':
         break

      else:
         print("Invalid choice. Please try again.")


if __name__ == "__main__":
   main()

```

#### Submission
- Submit two source code files named: `object_inherit.py` and `AdminUser.py`.

#### Assessment Criteria
- Correct implementation of the `AdminUser` class with proper inheritance from `AppUser`.
- Accurate creation and manipulation of objects in the driver file.
- Effective use of polymorphism and method overriding.
- Clear and well-documented code with appropriate comments.

#### Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code thoroughly to handle different user inputs and scenarios.

<hr> 

#### Additional Code
Demonstration Files

- Driver File

```python
"""
Module Name: Programming Lab 22
Description: Multiple Class Inheritance, Overridden Methods
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

from AppUser import AppUser
from apps.docs.python_exercises.labs.versions.code.AdminUser import AdminUser


def main():
   print(f'\nWelcome to Lab 22: Multiple Class Inheritance, Overridden Methods')

   while True:
      print("\n1. Create AppUser")
      print("2. Create AdminUser")
      print("3. Exit")
      choice = input("Enter your choice: ")

      if choice == '1':  # Create AppUser
         try:
            new_name = input("Preferred Name: ")
            new_contact = input("Contact Data: ")
            user = AppUser(new_name, new_contact)
            user.display_data()  # uses parent method
         except ValueError:
            print("Invalid input. Please enter valid data.")

      elif choice == '2':  # Create AdminUser
         try:
            new_name = input("Preferred Name: ")
            new_contact = input("Contact Data: ")
            new_role = input("Role: \n\tDefault=Guest, Client, Operator or Admin: ")
            new_id = int(input("User Number: "))
            admin_user = AdminUser(new_name, new_contact, new_role, new_id)
            admin_user.display_data()  # uses child overridden function
         except Exception as any_exception:
            print(f"This happened {any_exception}")

      elif choice == '3':
         break

      else:
         print("Invalid choice. Please try again.")


if __name__ == "__main__":
   main()

```

- Class File AdminUser.py

```python
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
    AdminUser extends AppUser adding user_role and user_id
    Attributes:
        user_role (str): .
        user_id (datetime): Logfile for user directory
    Methods:
        __init__(self, new_name='undefined', new_role='guest', new_id=-1): Initializes a new user with the provided name, role, and ID.
    """
    def __init__(self, new_name='unknown', contact='undefined', user_role='Guest', user_id=-1):
        """
        Initializes a new user with the provided name, role, and ID.
        Parameters:
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

```

<hr> 
