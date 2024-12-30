"""
The Lucky Number App
Description: Code Implemented from app_1_design.md
Clinton Garwood
September 2024
License: MIT
ChangeLog: Updated 'Aloha' to 'Hello'
"""

print(f'\nWelcome to the Lucky Name App')

# Get Information
user_data = input(f'Please enter your name: ')

# Manage Information Received
lucky_number = len(user_data)
user_proper = user_data.title()

# Reply to the User:
print(f'Hello {user_proper}, your lucky number is {lucky_number}')
