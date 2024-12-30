### Lab 24: "Object Serialization, Database, Object Store"

#### Assignment Overview
In this assignment, you will create a menu-driven program that explores different methods of data persistence, including serialization using Pickle, relational database storage with SQLite, and key-value storage using JSON. You can create objects of your own design or use `AppUser`, `AdminUser`, and `FullUser` classes from previous labs.

#### Learning Objectives
- Understand and implement object serialization using Pickle.
- Store and retrieve data using a relational database (SQLite).
- Work with key-value storage solutions using JSON.
- Develop a menu-driven program to handle different data storage methods.

#### Instructions
Explore options to save data (permanent) to files, databases and data stores. 

**24.1) Create File:**
1. Create a properly configured Python file named `object_save.py`.
2. At the top of the file, include any necessary classes (`AppUser`, `AdminUser`, `FullUser`) and libraries (`pickle`, `sqlite3`, `json`).
3. Define and call a `main()` function that takes no data and returns no data. Begin the function with a welcome message that introduces the exercise.
4. Implement a looped menu that provides the following options:
   - **Create and Save Objects using Pickle (Serialization):** Allow the user to create an object and save it to a file using the `pickle` module.
   - **Store Objects in a SQLite Database:** Provide an option to save and retrieve objects from an SQLite database.
   - **Store Objects using JSON (Key-Value Pairs):** Implement the ability to save and retrieve objects as JSON key-value pairs.
5. Test the menu to ensure all options for data persistence are functioning correctly and allow for smooth transitions between them.

**Example Menu:**
```python
def main():
    print(f'\nWelcome to Lab 24: Description: Data Persistence, Serialization ')

    # Create multiple objects of different types
    by_app = AppUser('iamme', 'textplease')
    by_admin = AdminUser('iamametoo', 'callme', 'Operator', 123)
    full_app = FullUser(by_app, user_role='Operator', user_id=234)
    full_admin = FullUser(by_admin)
    full_string = FullUser('me', 'seeme', 'admin', '01')
    user_pool = [by_app, by_admin, full_app, full_admin, full_string]

    while True:
        print("\n1. Generate Object Collection")
        print("2. Save objects using `pickle`")
        print("3. Save objects using JSON")
        print("4. Save objects using SQLite")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':  # Iterate Collection user_pool
            for each, object_found in enumerate(user_pool):
                if isinstance(object_found, FullUser):
                    print(f'\nFullUser Type')
                    object_found.display_data()
                elif isinstance(object_found, AdminUser):
                    print(f'\nAdmin Type')
                    object_found.display_data()
                elif isinstance(object_found, AppUser):
                    print(f'\nApp Type')
                    object_found.display_data()
        elif choice == '2':
            save_pickle()
            # try updating for save_pickle(user_pool)
        elif choice == '3':
            save_json()
            # try updating for save_json(user_pool)
        elif choice == '4':
            save_sql()
            # try updating for save_sql(user_pool)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

Example save_pickle() function
```python
def save_pickle():
    """
    This function create objects, serializes them (saves a file)
    then deserializing them to print out the deserialized value.
    The file 'users.pkl' is generated and contains encoded values.
    The JSON file contains plain text as JSON key:value pairs
    The `pickle` file likewise contains encoded text.
    Code in this function was generated with ChatGPT assistance
    :return:
    """

    users_dict = {
        1: AppUser("Alice", "alice@example.com"),
        2: AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
    }

    # Pickle the dictionary of user objects to a file
    with open('users_dict.pkl', 'wb') as f:
        pickle.dump(users_dict, f)

    # Unpickle the dictionary of user objects from the file
    with open('users_dict.pkl', 'rb') as f:
        loaded_users_dict = pickle.load(f)

    # Verify that the objects are correctly loaded
    for user_id, user in loaded_users_dict.items():
        print(f'User ID: {user_id}, User: {user.user_name}, Contact: {user.contact}')
        if isinstance(user, AdminUser):
            print(f'Role: {user.user_role}, ID: {user.user_id}')

    return
```

Example save_json() function
```python
def save_json():
    """
    This function creates a dictionary (key-value) store out of
    the metadata related to the data and its types.
    Two files are generated with the 'metadata dictionary' values
    `users_metadata.json` contains plain text as JSON key:value pairs
    `users_dict.pkl` contains encoded text of metadata dictionary
    Code in this function was generated with ChatGPT assistance
    :return:
    """
    import json

    # Sample data
    users = [
        AppUser("Alice", "alice@example.com"),
        AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
    ]

    # Create metadata
    metadata = []
    for user in users:
        metadata.append({
            'user_name': user.user_name,
            'contact': user.contact,
            'type': type(user).__name__,
            'user_role': getattr(user, 'user_role', None).value if getattr(user, 'user_role', None) else None,
            'user_id': getattr(user, 'user_id', None)
        })

    # Save metadata to a JSON file
    with open('users_metadata.json', 'w') as meta_file:
        json.dump(metadata, meta_file)

    # Save users to a pickle file
    with open('users.pkl', 'wb') as data_file:
        pickle.dump(users, data_file)

    # Load metadata to query
    with open('users_metadata.json', 'r') as meta_file:
        metadata = json.load(meta_file)

    # Query metadata
    for meta in metadata:
        print(meta)
        if meta['type'] == 'AdminUser':
            print(f"Admin User Found: {meta['user_name']}, Role: {meta['user_role']}")

    return
```

Example save_sql() function
```python
def save_sql():
    """
    The code in this function was generated with ChatGPT assistance
    :return:
    """
    import sqlite3
    import pickle

    # Sample data
    users = [
        AppUser("Alice", "alice@example.com"),
        AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
    ]

    # Create a SQLite database and table
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            contact TEXT,
            user_role TEXT,
            user_id INTEGER,
            data BLOB
        )
    ''')

    # Insert data into the database
    for i, user in enumerate(users):
        user_data = pickle.dumps(user)
        user_role = getattr(user, 'user_role', None)
        if user_role is not None:
            user_role = user_role.value  # Convert enum to string
        user_id = getattr(user, 'user_id', None)
        c.execute('''
            INSERT INTO users (id, user_name, contact, user_role, user_id, data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (i, user.user_name, user.contact, user_role, user_id, user_data))
        # `data` is created by anonymous or inline value passing when execute() runs
    conn.commit()

    # Query the database
    c.execute('SELECT user_name, contact, user_role, user_id FROM users WHERE user_role IS NOT NULL')
    for row in c.fetchall():
        print(row)

    # Load a specific user object
    c.execute('SELECT data FROM users WHERE user_name = ?', ('Bob',))
    user_data = c.fetchone()[0]
    user = pickle.loads(user_data)
    print(user.user_name, user.contact, user.user_role)

    return
```

#### Submission
- Submit one source code file named: `object_save.py`.

#### Assessment Criteria

- Correct implementation of object serialization using Pickle.
- Effective storage and retrieval of data using SQLite.
- Accurate use of JSON for key-value data storage.
- Clear and well-documented code with appropriate comments.
- Functional and user-friendly menu-driven program.

#### Additional Notes
- Ensure that your code is well-structured and adheres to Python coding standards.
- Thoroughly test your program to handle different scenarios for data persistence.

<hr> 

#### Additional Code
Demonstration Files

- Driver File

```python
"""
Module Name: Programming Lab 24
Description: Data Persistence, Serialization, Database, JSON Object Store
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

from AppUser import AppUser
from apps.docs.python_exercises.labs.versions.code.AdminUser import AdminUser
from FullUser import UserRole, FullUser

import pickle


def save_pickle():
   """
   This function create objects, serializes them (saves a file)
   then deserializing them to print out the deserialized value.
   The file 'users.pkl' is generated and contains encoded values.
   The JSON file contains plain text as JSON key:value pairs
   The `pickle` file likewise contains encoded text.
   Code in this function was generated with ChatGPT assistance
   :return:
   """

   users_dict = {
      1: AppUser("Alice", "alice@example.com"),
      2: AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
   }

   # Pickle the dictionary of user objects to a file
   with open('users_dict.pkl', 'wb') as f:
      pickle.dump(users_dict, f)

   # Unpickle the dictionary of user objects from the file
   with open('users_dict.pkl', 'rb') as f:
      loaded_users_dict = pickle.load(f)

   # Verify that the objects are correctly loaded
   for user_id, user in loaded_users_dict.items():
      print(f'User ID: {user_id}, User: {user.user_name}, Contact: {user.contact}')
      if isinstance(user, AdminUser):
         print(f'Role: {user.user_role}, ID: {user.user_id}')

   return


def save_json():
   """
   This function creates a dictionary (key-value) store out of
   the metadata related to the data and its types.
   Two files are generated with the 'metadata dictionary' values
   `users_metadata.json` contains plain text as JSON key:value pairs
   `users_dict.pkl` contains encoded text of metadata dictionary
   Code in this function was generated with ChatGPT assistance
   :return:
   """
   import json

   # Sample data
   users = [
      AppUser("Alice", "alice@example.com"),
      AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
   ]

   # Create metadata
   metadata = []
   for user in users:
      metadata.append({
         'user_name': user.user_name,
         'contact': user.contact,
         'type': type(user).__name__,
         'user_role': getattr(user, 'user_role', None).value if getattr(user, 'user_role', None) else None,
         'user_id': getattr(user, 'user_id', None)
      })

   # Save metadata to a JSON file
   with open('users_metadata.json', 'w') as meta_file:
      json.dump(metadata, meta_file)

   # Save users to a pickle file
   with open('users.pkl', 'wb') as data_file:
      pickle.dump(users, data_file)

   # Load metadata to query
   with open('users_metadata.json', 'r') as meta_file:
      metadata = json.load(meta_file)

   # Query metadata
   for meta in metadata:
      print(meta)
      if meta['type'] == 'AdminUser':
         print(f"Admin User Found: {meta['user_name']}, Role: {meta['user_role']}")

   return


def save_sql():
   """
   The code in this function was generated with ChatGPT assistance
   :return:
   """
   import sqlite3
   import pickle

   # Sample data
   users = [
      AppUser("Alice", "alice@example.com"),
      AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
   ]

   # Create a SQLite database and table
   conn = sqlite3.connect('users.db')
   c = conn.cursor()
   c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            contact TEXT,
            user_role TEXT,
            user_id INTEGER,
            data BLOB
        )
    ''')

   # Insert data into the database
   for i, user in enumerate(users):
      user_data = pickle.dumps(user)
      user_role = getattr(user, 'user_role', None)
      if user_role is not None:
         user_role = user_role.value  # Convert enum to string
      user_id = getattr(user, 'user_id', None)
      c.execute('''
            INSERT INTO users (id, user_name, contact, user_role, user_id, data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (i, user.user_name, user.contact, user_role, user_id, user_data))
      # `data` is created by anonymous or inline value passing when execute() runs
   conn.commit()

   # Query the database
   c.execute('SELECT user_name, contact, user_role, user_id FROM users WHERE user_role IS NOT NULL')
   for row in c.fetchall():
      print(row)

   # Load a specific user object
   c.execute('SELECT data FROM users WHERE user_name = ?', ('Bob',))
   user_data = c.fetchone()[0]
   user = pickle.loads(user_data)
   print(user.user_name, user.contact, user.user_role)

   return


def main():
   print(f'\nWelcome to Lab 24: Description: Data Persistence, Serialization ')

   # Create multiple objects of different types
   by_app = AppUser('iamme', 'textplease')
   by_admin = AdminUser('iamametoo', 'callme', 'Operator', 123)
   full_app = FullUser(by_app, user_role='Operator', user_id=234)
   full_admin = FullUser(by_admin)
   full_string = FullUser('me', 'seeme', 'admin', '01')
   user_pool = [by_app, by_admin, full_app, full_admin, full_string]

   while True:
      print("\n1. Generate Object Collection")
      print("2. Save objects using `pickle`")
      print("3. Save objects using JSON")
      print("4. Save objects using SQLite")
      print("5. Exit")
      choice = input("Enter your choice: ")

      if choice == '1':  # Iterate Collection user_pool
         for each, object_found in enumerate(user_pool):
            if isinstance(object_found, FullUser):
               print(f'\nFullUser Type')
               object_found.display_data()
            elif isinstance(object_found, AdminUser):
               print(f'\nAdmin Type')
               object_found.display_data()
            elif isinstance(object_found, AppUser):
               print(f'\nApp Type')
               object_found.display_data()
      elif choice == '2':
         save_pickle()
         # try updating for save_pickle(user_pool)
      elif choice == '3':
         save_json()
         # try updating for save_json(user_pool)
      elif choice == '4':
         save_sql()
         # try updating for save_sql(user_pool)
      elif choice == '5':
         break
      else:
         print("Invalid choice. Please try again.")


if __name__ == "__main__":
   main()

```

<hr> 