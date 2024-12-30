# Code Demo for 13 Lecture
# Working with Python Strings
# CIS 135 - Code Demo File


# Lecture example showing string contatenation
firstName = "Peter"
lastName = "Parker"
print("\nString Contcatenation in Pyton uses the + operator")
print(f'First Name = {firstName}')
print(f'Last Name = {lastName}')
print("Peter Parker can be concatenated as 'firstName' + ' ' + 'lastName'")
print("Hello,", firstName + ' ' + lastName)

# Example slicing JJC
JJC = "Joliet Junior College"
print('\nJJC = "Joliet Junior College"')
print("\nExtract 'Joliet' from the variable JJC")
print(JJC[0:6]) # this returns the first six characters

print("\nExtract 'College' from the variable JJC")
print(JJC[-7:]) # this returns the final seven characters

print("\nExtract 'Junior' from the variable JJC")
print(JJC[7:-7]) # this returns the final seven characters

alphas = 'abcdefghi'
print(f'\nThe variable alphas = {alphas}')
print('alphas[1:3] extract characters ', alphas[4:8])
print('alphas[:3] = will extract characters ', alphas[:3])
print('alphas[-2:] = will extract characters ', alphas[-2:])
print('alphas[-3:-2] = will extract characters ', alphas[-3:-2])

this_string = "     some text      "
print(this_string.lstrip())
print(this_string.rstrip())