### Lab 14: "Dictionaries as Key:Value Pairs of Data"

#### Assignment Overview
In this lab, you will work with Python dictionaries to represent a collection of data. You will initialize a set of tuples, convert them into a nested dictionary, and perform various operations to access and query the data.
We will handle data as is represented by the table below:

| username | password | strength |
|:--------|:---------|:--------|
| admin | x2zm#S.y | strong |
| manager | xr,ly.zn | strong | 
| editor | xrytnz   | fair |
| creator | xyzzts   | fair | 
| guest | xrs      | weak | 
| visitor | lxm      | weak | 

#### Learning Objectives
- Understand how to initialize and manipulate dictionaries in Python.
- Learn to convert tuples and lists into dictionaries.
- Practice accessing and querying data stored in nested dictionaries.

#### Instructions
**14.1) Create File**
- Create a properly formatted Python file named `dictionary_key_value.py`

**14.2) Define the main Function**
- Define a function named `main`, which contains a welcome statement and initializes the user data as follows:
```python
def main():
    print(f'\nWelcome to Lab 14: Dictionaries Contain Key-Value Pair Data.')

    # Initialize user data tuples and matrix 
    user_1 = ('admin', 'x2zm#S.y', 'strong')
    user_2 = ('manager', 'xr,ly.zN', 'strong')
    user_3 = ('editor', 'xrytnz', 'fair')
    user_4 = ('creator', 'xyzzts', 'fair')
    user_5 = ('guest', 'xrs', 'weak')
    user_6 = ('visitor', 'lxm', 'weak')
    user_list = [user_1, user_2, user_3, user_4, user_5, user_6]

    # Your code goes here
    
    return

main()

```

**14.3) Simple Dictionary**
Initialize a new empty dictionary named `sample_dict` and populate it with data from one of the tuples:
```python
sample_dict = dict()
sample_dict['username'] = user_5[0]
sample_dict['passkey'] = user_5[1]
sample_dict['security'] = user_5[2]

print(f'\nSample Dictionary is\n\t{sample_dict}')
print(f'\tUsername is {sample_dict["username"]}')
print(f'\tPasskey is {sample_dict["passkey"]}')
print(f'\tSecurity is {sample_dict["security"]}')
```

**14.4) Nested Dictionary**
Initialize a new dictionary named `user_dictionary` and populate it with data from `user_list`:
Notice in the code below that data is extracted from the list by index where the [1] value is aligned with 'passkey', the [2] value is aligned with 'security', and finally the [0] value is used as the name for the nested dictionary records. The code creates a new temporary dictionary (with each pass of the loop) to hold these values. The temporary dictionary is then added to user_dictionary.
```python
user_dictionary = dict()
for each, value in enumerate(user_list):
    temp_dict = {
        'passkey': value[1],
        'security': value[2]
    }
    user_dictionary[f'{value[0]}'] = temp_dict

print(f'\nValues of user_dictionary')
for username, user in user_dictionary.items():
    print(f'\tusername: {username}, passkey: {user["passkey"]}, security: {user["security"]}')
```

**14.5) Query the Dictionary**
Query the dictionary to find users with a "strong" passphrase:
Iterating a dictionary has a syntax different than lists. Notice that there is NO enumerate() function, and that the dictionary name has a .items() appended to the end of it. Also notice that the loop variables 'username, user' differ as well. Here 'username' is not an index/integer, but is the main name of the nested collection. The variable 'user' contains a dictionary of the inner collections values.
```python
print(f'\nUsers with Secure Passwords')
for username, user in user_dictionary.items():
    if user["security"] == "strong":
        print(f'\t{username} has a {user["security"]} password.')
```

Query the dictionary to find users with passkeys shorter than 8 characters:
```python
print(f'\nUsers with Poor Passwords')
for username, user in user_dictionary.items():
    if len(user["passkey"]) < 8:
        print(f'\t{username} passkey length is only {len(user["passkey"])} characters long.')
```

#### Submission
- Submit a single source code file named: `dictionary_key_value.py`.

#### Assessment Criteria
- Correctly initialized and populated dictionaries.
- Accurate access and print statements for dictionary values.
- Correct implementation of the nested dictionary.
- Accurate query results for users with strong and poor passwords.

#### 6) Additional Notes
- Ensure your code is well-commented to explain the functionality.
- Follow best practices for variable naming and code organization.
- Test your code to verify the correctness of the output.

<hr>

#### Additional Code
Demonstration File 

```python
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
    user_1 = ('admin', 'x2zm#S.y', 'strong')
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

```

<hr>
