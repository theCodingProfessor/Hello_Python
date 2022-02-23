# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# file_create_write_clinton.py
# CIS-135 Python
# Assignment #22 File Open, Write and Close

# Create a Python script file (named file_write.py) that demonstrates the basic
# elements of opening, writing-to and closing a text file.

# Rubric 1 Point:
# Create a function named createFile that takes a string variable (for the name of the
# file), as its only parameter. Use Python's built-in open() function with the 'x' (for create)
# mode to create the file. Close the file handle before exiting the function.
def createFile(file_name):
  create_new = open(file_name, 'x')
  create_new.close()
  return

# Rubric 2 Points:
# Create a function named writeData that takes a string variable (for the name of the
# file), as its only parameter. Use Python's built-in open() function with the 'w' and 't'
# modes to write the following four lines of text to the file
# Steps to file management:
#   1: Open a file.
#   2: Read or write data.
#   3: Close the file.
# Make sure to properly format your file for new lines and indentation.
# Close the file handle before exiting the function.
def writeData(file_name):
  write_data = open(file_name, 'wt')
  write_data.write("Steps to file management:\r")
  write_data.write("\t1: Open a file.\r")
  write_data.write("\t2: Read or write data.\r")
  write_data.write("\t3: Close the file.\r")
  write_data.close()
  return

# Rubric 1 Point:
# Create a function named printData that takes a string variable (for the name of the
# file), as its only parameter. Use Python's built-in open() function with the 'r'
# mode to loop through the file and print the text found in the file to the screen.
# Close the file handle before exiting the function.
def printData(file_name):
  print_file = open(file_name, 'r')
  for line in print_file:
    print(line)
  print_file.close()
  return

# Rubric 1 Point:
# Create a function named main that will create a variable named file_name to hold the string
# value "create_this_file.txt". Properly call the three functions passing the value of
# the file name to each. Finally call the main function.
def main():
  file_name = "create_this_file.txt"
  createFile(file_name)
  writeData(file_name)
  printData(file_name)
  return

main()