"""
Module Name: Programming Lab 24
Description: Data Persistence, Serialization, Database, JSON Object Store
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

from AppUser import AppUser
from AdminUser import AdminUser
from FullUser import UserRole, FullUser

import pickle


def save_pickle(user_dictionary_list):
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
        pickle.dump(user_dictionary_list, f)

    # Unpickle the dictionary of user objects from the file
    with open('users_dict.pkl', 'rb') as f:
        loaded_users_dict = pickle.load(f)

    # Verify that the objects are correctly loaded
    for user_id, user in loaded_users_dict.items():
        print(f'User ID: {user_id}, User: {user.user_name}, Contact: {user.contact}')
        if isinstance(user, AdminUser):
            print(f'Role: {user.user_role}, ID: {user.user_id}')

    return


def save_json(users):
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
    # users = [
    #     AppUser("Alice", "alice@example.com"),
    #     AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
    # ]

    # Create metadata
    metadata = []
    for user in users:
        try:
            metadata.append({
                'user_name': user.user_name,
                'contact': user.contact,
                'type': type(user).__name__,
                'user_role': getattr(user, 'user_role', None).value if getattr(user, 'user_role', None) else None,
                'user_id': getattr(user, 'user_id', None)
            })
        except AttributeError:
            metadata.append({
                'user_name': user.user_name,
                'contact': user.contact,
                'type': type(user).__name__,
                'user_role': 'unknown',
                'user_id': -1
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


def save_sql(users):
    """
    The code in this function was generated with ChatGPT assistance
    :return:
    """
    import sqlite3
    import pickle

    # Sample data
    # users = [
    #     AppUser("Alice", "alice@example.com"),
    #     AdminUser("Bob", "bob@example.com", UserRole.ADMIN, 1)
    # ]

    # Create a SQLite database and table
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # c.execute('''
    #     CREATE TABLE IF NOT EXISTS users (
    #         id INTEGER PRIMARY KEY,
    #         user_name TEXT,
    #         contact TEXT,
    #         user_role TEXT,
    #         user_id INTEGER,
    #         data BLOB
    #     )
    # ''')
    #
    # # Insert data into the database
    # for i, user in enumerate(users):
    #     user_data = pickle.dumps(user)
    #     try:
    #         user_role = user.user_role.value
    #         user_id = user.user_id.value
    #     except AttributeError:
    #         user_role = 'Not Assigned'
    #         user_id = 12 + i
    #     c.execute('''
    #         INSERT INTO users (id, user_name, contact, user_role, user_id, data)
    #         VALUES (?, ?, ?, ?, ?, ?)
    #     ''', (i, user.user_name, user.contact, user_role, user_id, user_data))
    #     # `data` is created by anonymous or inline value passing when execute() runs
    # conn.commit()

    # Query the database
    c.execute('SELECT user_name, contact, user_role, user_id FROM users WHERE user_role IS NOT NULL')
    for row in c.fetchall():
        print(row)

    # Load a specific user object
    # c.execute('SELECT data FROM users WHERE user_name = ?', ('Bob',))
    # user_data = c.fetchone()[0]
    # user = pickle.loads(user_data)
    # print(user.user_name, user.contact, user.user_role)

    return


def main():
    print(f'\nWelcome to Lab 24: Description: Data Persistence, Serialization ')

    # Create multiple objects of different types
    by_app = AppUser('iamme', 'textplease')
    by_admin = AdminUser('iamametoo', 'callme', 'Operator', 7)
    full_app = FullUser(by_app, user_role='Operator', user_id=6)
    full_admin = FullUser(by_admin)
    full_string = FullUser('me', 'seeme', 'admin', 5)
    user_pool = [by_app, by_admin, full_app, full_admin, full_string]

    user_dictionary_list = []
    for user in user_pool:
        try:
            user_dictionary_list.append({
                'user_name': user.user_name,
                'contact': user.contact,
                'type': type(user).__name__,
                'user_role': user.user_role,
                'user_id': user.user_id})
        except AttributeError:
            user_dictionary_list.append({
                'user_name': user.user_name,
                'contact': user.contact,
                'type': type(user).__name__,
                'user_role': 'unknown',
                'user_id': -1})

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
            save_pickle(user_dictionary_list)
            # try updating for save_pickle(user_pool)
        elif choice == '3':
            save_json(user_pool)
            # try updating for save_json(user_pool)
        elif choice == '4':
            save_sql(user_pool)
            # try updating for save_sql(user_pool)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
