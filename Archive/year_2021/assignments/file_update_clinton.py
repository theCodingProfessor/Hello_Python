# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# file_update_clinton.py
# CIS-135 Python
# Assignment #23 File Append in Python

# Create a Python script file (named file_update.py) that demonstrates the basic
# elements of updating (using append) information in a text file.

# Rubric 1 Point:
# Create a function named countLines which opens the text file created in exercise #22
# (named 'create_this_file.txt') in order to count the lines of data in that file. In this
# function create a counter that is incremented for each line found in the file. This
# function should take a single parameter (a string variable with the name of the file),
# and the integer counter variable.
def countLines(file_name):
  get_count = 0
  count_file = open(file_name, 'r')
  for line in count_file:
    get_count += 1
  count_file.close()
  return get_count # 4, #5, #6

# Rubric 1 Point:
# Create a function named appendFile that takes both the string variable name (file_name)
# as well as the counter variable returned from countLines. Use Python's built in open()
# function in 'a' append mode to add (append) a new line of data to the file which reads:
# "create_this_file.txt had 4 lines of data, now it will have 5". Use variables to print
# the file name and the numbers (i.e., 4 or 5...) into the file. Be sure to call close()
# before returning from the function.
def appendFile(file_name, original_count):
  write_data = open(file_name, 'a')
  write_data.write(f'{file_name} had {original_count} lines of data, and now has {original_count + 1}\r')
  write_data.close()
  return

# Rubric 1 Point:
# Create a function named confirmAppend that takes the string variable name (file_name)
# and prints the result of the text file to the screen. Be sure to close the file before
# the function returns.
def confirmAppend(file_name):
  print_file = open(file_name, 'r')
  for line in print_file:
    print(line)
  print_file.close()
  return

# Rubric 2 Points:
# Create a function named appendToTen that uses a loop and the three functions
# described above to update 'create_this_file.txt' in such as way that it will eventually
# contain the string, "create_this_file.txt had 9 lines of data, and now has 10"
# Once the file contains this information, print the contents of the file to the screen.
# The function appendToTen should not take any data (i.e., has an empty parameter list),
# and will not return any data to the caller. At the very end of this script file
# call appendToTen
def appendToTen():
  update_counter = 0
  file_name = 'create_this_file.txt'
  while update_counter < 9:
    update_counter = countLines(file_name)
    appendFile(file_name, update_counter)
  confirmAppend(file_name)
  return

appendToTen()
