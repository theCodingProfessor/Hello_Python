"""
Module Name: Programming Lab 14
Description: Dictionary Data Structures
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def main():
    print(f'\nWelcome to Lab 14: Dictionaries Contain Key:Value Pair Data.')

    # Initialize user data
    user_1 = ('admin', 'xZzm|s.y', 'strong')
    user_2 = ('manager', 'xr,ly.zN', 'strong')
    user_3 = ('editor', 'xrytnz', 'fair')
    user_4 = ('creator', 'xyzzts', 'fair')
    user_5 = ('guest', 'xrs', 'weak')
    user_6 = ('visitor', 'lxm', 'weak')
    user_list = [user_1, user_2, user_3, user_4, user_5, user_6]

    # Parse values from user_list into user_dictionary
    sample_dict = dict()  # also can be sample_dict = {}
    sample_dict['username'] = user_5[0]
    sample_dict['passkey'] = user_5[1]
    sample_dict['security'] = user_5[2]

    print(f'\nSample Dictionary is\n\t{sample_dict}')
    print(f'\tUsername from Sample Dictionary is {sample_dict["username"]}')
    print(f'\tPasskey from Sample Dictionary is {sample_dict["passkey"]}')
    print(f'\tSecurity from Sample Dictionary is {sample_dict["security"]}')

    # Create the user_access dictionary
    user_dictionary = dict()

    # Given a matrix (list of list) we will need to use a more complex
    # system to lift-load values from the list to the dictionary
    for each, value in enumerate(user_list):
        temp_dict = {
            'passkey': value[1],
            'security': value[2]}
        user_dictionary[f'{value[0]}'] = temp_dict

    print(f'\nValues of user_dictionary')
    for username, user in user_dictionary.items():
        print(f'\tusername: {username}, passkey: {user["passkey"]}, security: {user["security"]}')

    # Given the populated dictionary, we can now 'ask' the collection
    # to return values by word/key.

    # Query the collections for users with strong passkeys
    print(f'\nUsers with Secure Passwords')
    for username, user in user_dictionary.items():
        if user["security"] == "strong":
            print(f'\t{username} has a {user["security"]} password.')

    # Retrieve users who should use a more secure passkey
    print(f'\nUsers with Poor Passwords')
    for username, user in user_dictionary.items():
        if len(user["passkey"]) < 8:
            print(f'\t{username} passkey length is only {len(user["passkey"])} characters long.')

    return


main()
