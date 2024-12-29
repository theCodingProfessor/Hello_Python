### Lab 20: "Python Class, Data Members and Methods"

#### Assignment Overview
In this assignment, you will explore creating a simple Python class that allows for the instantiation of an object of that class type. The class will include a constructor, getters, setters, and a method to display its data in a formatted manner.

#### Learning Objectives
- Understand the structure and purpose of a Python class.
- Implement class constructors, data members, and methods.
- Use getter and setter methods to manipulate class data members.
- Create and call methods to display class data.

#### Instructions

**20.1) Create File**
- Create a properly formatted Python file named `class_basic.py`

**20.2) Define the Class**
- Above the `main` function, create a Python class named `UserData` that contains three data members: `user_name` (string), `user_role` (string), `user_id` (int). Make sure your data members, constructor and class methods are all indented to the same level. 

**20.3) Implement the Constructor**
The class constructor, `__init__()`, should not take any data. Within the constructor, print a message: 'The UserData class constructor has been called.'

**20.4) Define Setter and Getter Methods**
Create the following setter and getter methods (all equally indented):

**20.4.1) Setter for `user_name`**
```python
def set_user_name(self, name):
    """
    Set the user_name
    :param name: User name (string)
    :return: None
    """
    self.user_name = name
```

**20.4.2) Getter for `user_name`**
```python
def get_user_name(self):
    """
    Get the user_name
    :return: User name (string)
    """
    return self.user_name
```

**20.4.3) Setter for `user_role`**
```python
def set_user_role(self, role):
    """
    Set the user_role.
    :param role: User role (string)
    :return: None
    """
    self.user_role = role
```

**20.4.4) Getter for `user_role`**
```python
def get_user_role(self):
    """
    Get the user_role.
    :return: User role (string)
    """
    return self.user_role
```

**20.4.5) Setter for `user_id`**
```python
def set_user_id(self, user_id):
    """
    Set the user_id
    :param user_id: User ID (int)
    :return: None
    """
    self.user_id = user_id
```

**20.4.6) Getter for `user_id`**
```python
def get_user_id(self):
    """
    Get the user_id
    :return: User ID (int)
    """
    return self.user_id
```

**20.5) Define `display_data` Method**
Create a `display_data` method that prints a formatted presentation of all three data members.
```python
def display_data(self):
    """
    Displays the user data in a formatted manner.
    :return: None
    """
    print(f'User Name: {self.user_name}')
    print(f'User Role: {self.user_role}')
    print(f'User ID: {self.user_id}')
```

**20.6) Define Main Function**
- Create and call a function named `main` that takes no data and returns no data.
- Inside `main`, create a new object of type `UserData`.
- Call the setter and getter methods to manipulate and retrieve the object's data members.
- Call `display_data` to print the formatted data.

```python
def main():
    print(f'\nWelcome to Lab 20: Simple Class has Data and Methods')

    user = UserData()
    
    user.set_user_name("Alice")
    print(user.get_user_name())
    
    user.set_user_role("Administrator")
    print(user.get_user_role())
    
    user.set_user_id(12345)
    print(user.get_user_id())
    
    user.display_data()

if __name__ == "__main__":
    main()
```

#### Submission
Submit a single source code file named: `class_basic.py`.

#### Assessment Criteria
- Correct implementation of the class with data members, constructor, setter, and getter methods.
- Proper use of class methods to manipulate and display data.
- Accurate implementation of the main function to demonstrate class functionality.
- Clear and well-documented code with appropriate comments.

#### Additional Notes
- Ensure your code is properly formatted and follows Python coding standards.
- Test your code to verify that the class methods work as expected.

<hr>

#### Additional Code: 

Sample Class File
```python
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
```

<hr>

#### Additional Code
Demonstration File 

```python
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
    print(user.get_user_name())

    user.set_user_role("Administrator")
    print(user.get_user_role())

    user.set_user_id(12345)
    print(user.get_user_id())

    user.display_data()
    return


if __name__ == "__main__":
    main()

```
