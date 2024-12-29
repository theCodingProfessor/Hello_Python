### Lab 23: "Polymorphism and Multiple Inheritance"

#### Assignment Overview
In this assignment, you will extend your skills in object-oriented programming by creating a new class `FullUser` that inherits from `AdminUser`, which itself inherits from `AppUser`. You will explore polymorphism and object inheritance, adding new functionalities and data members to the `FullUser` class, and using an overloaded parameter list for the constructor.

#### Learning Objectives

- Understand and implement class inheritance in Python.
- Utilize polymorphism to override methods in derived classes.
- Practice creating and managing class objects with complex constructors.
- Work with enumerations for data validation.

#### Instructions
Explore multi-inherited classes and ENUM, a static list.

**23.1) Create File:** - Create the first (of two) formatted Python file `FullUser.py`
1. Use object inheritance to define `FullUser` as a child class of `AdminUser`, which itself is a child of `AppUser`.
2. Add a new data member `user_directory` in `FullUser`. Set it as a string with the format `directory_<userid>`:
3. Create getter and setter methods for `user_directory`. Override the display method to present all data members of `FullUser`.
4. Implement the `FullUser` class constructor to accept either `*args` (a list) and/or `**kwargs` (a dictionary). Handle objects for lists first (like the `AppUser` object), followed by any key-value pairs needed.
5. Ensure the `FullUser` class updates the `last_seen` attribute.

```python
from AppUser import AppUser
from apps.docs.python_exercises.labs.versions.code.AdminUser import AdminUser

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
         super().__init__(admin_user.user_name, admin_user.contact, user_role=admin_user.user_role,
                          user_id=admin_user.user_id)
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
         # Handle case where individual strings are passed
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

```

**23.2) Create File: object_overloading.py**
1. Create the second (of two) Python file named `object_overloading.py`
2. At the top of the file, include the `AdminUser` class.
3. Define and call a `main()` function that takes no data and returns no data.
4. Inside `main`, create two lists: one for objects including `AppUser` and `AdminUser`, and another list just for `FullUser` objects.
5. Implement a menu loop that allows the user to:
   - Create `AppUser`
   - Create `AdminUser`
   - Create `FullUser` from string input
   - Create `FullUser` from an `AppUser` or `AdminUser` object
6. When a new `FullUser` is created, add the object to the `valid_users` list. If a `FullUser` is created from an existing object, use `pop()` to remove the object from the `user_pool` list.
7. Test the script by running `object_overloading.py` and creating a new object of each type to ensure the overloaded parameter feature works correctly.

Scaffold `main()` function:
```python
def main():
    user_pool = []
    valid_users = []

    while True:
        print("\nMenu:")
        print("1. Create AppUser")
        print("2. Create AdminUser")
        print("3. Create FullUser from string input")
        print("4. Create FullUser from an AppUser or AdminUser object")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Code to create AppUser and add to user_pool
            pass
        elif choice == '2':
            # Code to create AdminUser and add to user_pool
            pass
        elif choice == '3':
            # Code to create FullUser from string input and add to valid_users
            pass
        elif choice == '4':
            # Code to create FullUser from an existing object
            pass
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

Extended Example `main()` function:

```python
from AppUser import AppUser
from apps.docs.python_exercises.labs.versions.code.AdminUser import AdminUser
from FullUser import UserRole, FullUser


def main():
   print(f'\nWelcome to Lab 23: Polymorphism and Overloaded Object Constructor')

   user_pool = []
   valid_users = []
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

      if choice == '4':  # Create AppUser Direct Input
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


if __name__ == "__main__":
   main()

```

#### Submission
- Submit two source code files: `object_overloading.py` and `FullUser.py`.

#### Assessment Criteria

- Correct implementation of the `FullUser` class with proper inheritance from `AdminUser`.
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
Module Name: Programming Lab 23
Description: Polymorphism and Overloaded Object Constructor
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

from AppUser import AppUser
from apps.docs.python_exercises.labs.versions.code.AdminUser import AdminUser
from FullUser import UserRole, FullUser


def main():
   print(f'\nWelcome to Lab 23: Polymorphism and Overloaded Object Constructor')

   user_pool = []
   valid_users = []
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

      if choice == '4':  # Create AppUser Direct Input
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


if __name__ == "__main__":
   main()

```

- Class File - FullUser.py

```python
"""
Module Name: Programming Lab 23
Description: FullUser Class, inherits AdminUser override display_data.
Author: Clinton Garwood
Date: August 2024
License: MIT
Classes: FullUser - new user_directory, update last_seen
"""
from AppUser import AppUser
from apps.docs.python_exercises.labs.versions.code.AdminUser import AdminUser

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
         super().__init__(admin_user.user_name, admin_user.contact, user_role=admin_user.user_role,
                          user_id=admin_user.user_id)
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
         # Handle case where individual strings are passed
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

```

<hr>
