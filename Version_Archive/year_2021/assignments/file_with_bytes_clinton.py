# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# file_copy_clinton.py
# CIS-135 Python
# Assignment #25 Open File With Bytes

import os

# Create a Python script file (named file_with_bytes.py) that demonstrates the basics
# of using 'with open()' to manage file handling, and show the use of 'b' byte mode.

# Rubric 1 Point:
# Create a function named readText which takes a single string variable named
# path_to_file and; 1) Opens the file; 2) Prints the contents and; 3) closes
# the file automatically
def readText(path_to_file):
  with open(path_to_file, 'r') as rt:
    print(rt.read())
  # implied rt.close()
  return

# Rubric 1 Point:
# Create a function named readBytes which takes a single string variable named
# path_to_file and; 1) Opens the file; 2) Prints the content, and 3) closes the
# file automatically
def readBytes(path_to_file):
  with open(path_to_file, 'rb') as rb:
    print(rb.read())
  # implied rb.close()
  return

# Rubric 1 Point:
# Create a function called copyBytes that takes a two string variables copy_from
# which is path to the initial file, and copy_to which is the path (and file name)
# of where the copied file should be saved. The copy will take the (existing) text
# file, and copy it as a byte file (this is not a human readable format). The new
# file be saved into the same directory as the source file.
def copyBytes(copy_from, copy_to):
  if os.path.exists(copy_from):
    with open(copy_from,'rb') as read_from:
      with open(copy_to,'wb') as write_to:
        for line in read_from:
          write_to.write(line)
     # implied close for write.to
  # implied close for read_from

# Rubric 2 Points:
# Create a function called copyAndPrint that organizes the three functions
# described above into a single workflow. The workflow will create a new file
# named byte_copy.bytes by making a byte copy of the 'copied_file.txt' which
# was created in assignment 24. (Pay attention to the directory structure and
# use the os library to navigate into the folder). Once the file is copied,
# print the content of each file to the screen.
def copyAndPrint():
  starting_path = os.getcwd()
  os.chdir(starting_path)
  if os.path.exists("new_folder"):
    os.chdir("new_folder")
  copy_from = "copied_file.txt"
  copy_to = "byte_copy.bytes"
  copyBytes(copy_from, copy_to)
  readText(copy_from)
  readBytes(copy_to)
  return

copyAndPrint()
