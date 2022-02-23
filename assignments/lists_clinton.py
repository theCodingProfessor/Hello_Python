# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# lists_clinton.py
# CIS-135 Python
# Assignment #16 Python Lists and For Loops

# Rubric 1 point:
# Establish a Python list named py_list with the following pieces of data:
# 1,2,4,8,16,32,64,128,256,512. Print the list to the screen
py_list = [1,2,4,8,16,32,64,128,256,512]
print(py_list)
print()

# Rubric 1 point:
# Create and call a function named: "printList" which has
# a for-loop that will access each piece of data in the list,
# printing each piece of data found to the screen with each pass.
def printList(py_list):
  for each in py_list:
    #print("Found", each, "in py_list")
    print(f"Found {each} in py_list")
  return

# First request to call printList
print("First call to printList")
printList(py_list)

# Rubric 1 point:
# Declare another function named updateList (that takes py_list) as
# its only incoming parameter and uses a modified for-loop to iterate
# through the list, doubling (item x 2) each item found. Return the
# list to the caller at the end of the function.
def updateList(py_list):
  # This first code block will not work?
  # can you figure out why?
  # for each in py_list:
  #  py_list[each] = each * 2
  # This second code block does work, but it is bulky
  # counter = 0
  # for each in py_list:
  #  py_list[counter] = each * 2
  #  counter = counter + 1
  #counter += 1
  # final option is to use the built-in Python
  # enumerate() function
  for count, value in enumerate(py_list):
    py_list[count] = value * 2
  return py_list

py_list = updateList(py_list)
print()

# Rubric 1 point:
# Call the printlist function again,
# printing out the values in the list.
# Final call to printList
print("Final call to printList")
printList(py_list)
