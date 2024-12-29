# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# file_copy_clinton.py
# CIS-135 Python
# Assignment #24 File Copy in Python

import os
import shutil

# Create a Python script file (named file_copy.py) that demonstrates the basics
# of navigating a file system using os to retrieve and manage (copy) files with Python.

# Rubric 1 point:
# Create a function named createFolder which takes a single string variable
# start_file_path and then; 1) Prints the file system path (where this file is
# running from), 2) Creates a new folder inside of the current directory named
# (new_folder), 3) Navigates into new_folder; and 4) Prints out the path while
# inside of new_folder.
def createFolder():
  # 1) Print the file system path
  print("\nThe beginning os file system path is: ", os.getcwd())
  # 2) Create a new folder inside of the current directory (named new_folder)
  new_folder = "new_folder"
  os.mkdir(new_folder)
  # 3) Navigate into the newly created directory
  os.chdir(new_folder)
  # 1) Print out the path from inside the new_folder directory
  print("The os file system path inside new_folder is: ", os.getcwd(), "\n")
  return

# Rubric 1 Point:
# Create a function called copyRename that takes a single string variable (which is the
# initial file path. The function will retrieve the text file "create_this_file.txt"
# which was updated in exercise #23, and copy that file into the new_folder directory.
# Use the function createFolder() to create and navigate into that folder. Do not recode
# that navigation process.
def copyRename(starting_path):
  os.chdir(starting_path)
  if os.path.exists("new_folder"):
    copy_from = starting_path + "\\create_this_file.txt"
    print(f'The old (original) file name and path is: {copy_from}')
    copy_to = starting_path + "\\new_folder" + "\\copied_file.txt"
    shutil.copy(copy_from, copy_to)
    print(f'\nThe new (renamed) file name and path is: {copy_to}')

# Rubric 1 Point:
# Create a function called moveFile that takes a single string variable (which is the
# initial file path. The function will retrieve the text file "create_this_file.txt"
# which was updated in exercise #23, and copy that file into the new_folder directory.
# Use the function createFolder() to create and navigate into that folder. Do not recode
# that navigation process. Once this function is complete, the file will no longer
# reside in the original file directory, but will reside in new_folder
def moveFile(starting_path):
  os.chdir(starting_path)
  if os.path.exists("new_folder"):
    #print("new_folder found")
    copy_from = starting_path + "\\create_this_file.txt"
    #print(f'The old (original) file name is: {copy_from}')
    copy_to = starting_path + "\\new_folder" + "\\create_this_file.txt"
    shutil.copyfile(copy_from, copy_to)
    print('\nThe original file has been moved by shutil.copyfile()')

# Rubric 1 Point:
# Create a function called moveAndCopyFile that organizes the three functions
# described above into a single workflow. The workflow will include creating
# a file directory named new_folder), will save a renamed copy of the original
# text file create_this_file.txt into new_folder, and finally will move the
# original file into new_folder, and then delete the original file from the
# starting directory. The moveAndCopyFile function will not take any data
# (i.e., has an empty parameter list) and will not return any data.
def moveAndCopyFile():
  starting_path = os.getcwd()
  createFolder()
  copyRename(starting_path)
  moveFile(starting_path)
  os.chdir(starting_path)
  if os.path.exists("create_this_file.txt"):
    os.remove("create_this_file.txt")
  print('\nThe original file has been removed from the assignments directory')
  return

moveAndCopyFile()
