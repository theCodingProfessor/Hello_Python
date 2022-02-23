# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_9_clinton.py
# CIS-135 Python
# Homework Assignment #9 – Inventory File Management

# Code Summary: Python application that allows a user to
# record and retrieve inventory data by creating, writing
# to and reading from a plain text file. A main menu will
# prompt a user to select 1) Add an Item; 2) Print the Inventory
# or 3) Exit the system. When the user selects “Add an Item”,
# the user is asked to provide three pieces of information
# (name, quantity and cost) for that item. The data is then
# saved into the text file. The print option from the main menu
# reads all the data currently in the file, and prints it to
# the screen as a nicely formatted table. In addition to printing
# out the data found, a total value (quantity * cost) of each item
# is displayed, as are the total number of items in the inventory,
# and the total value of the entire inventory.

# Change-Log: No updates logged yet

def write_data(name_of_file):
  incoming_inventory_list = []
  # Get the data from the user:
  # Prompt the user for the item name, item quantity, item value/cost
  incoming_inventory_list.append(input("\t\t\tWhat is the name of this item? "))
  incoming_inventory_list.append(input("\t\t\tHow many items of this type? "))
  incoming_inventory_list.append(input("\t\t\tCost for one of these items? "))
  # open the file (name_of_file)
  write_data = open(name_of_file, 'a')
  # write to file (append the data at the end of the text file)
  write_data.write(str(incoming_inventory_list[0]))
  write_data.write(str(", "))
  write_data.write(str(incoming_inventory_list[1]))
  write_data.write(str(", "))
  write_data.write(str(incoming_inventory_list[2]))
  write_data.write(str(", "))
  write_data.write(str("\n"))
  # close the file
  write_data.close()
  return

def print_data(inventory_read):
  total_items = 0 # (integer) for the number of all items in inventory
  grand_total_value = 0 # (float) for the total value of all inventory items
  if len(inventory_read) == 0:
    print("\n\t\tNo data found in inventory. Please Select Option 1 to add items.\n")
  else:
    print("\n\t\t{:<15}{:>12}{:>13}{:>14}".format("Item Name","Quantity","Item Value","Total Value"))
    for counter, value in enumerate(inventory_read):
      # extract name, quantity and value from each nested list
      name = inventory_read[counter][0]
      quantity = int(inventory_read[counter][1])
      value = float(inventory_read[counter][2])
      # update stock value
      stock_value = value * quantity
      # update total items
      total_items = total_items + quantity
      # update grand total value
      grand_total_value = grand_total_value + stock_value
      print("\t\t{:<15}{:>12n}{:>13,.2f}{:>14,.2f}".format(name, quantity, value, stock_value))
  print("\t\tTotal items in inventory is {:,}".format(total_items))
  print("\t\tGrand total value of inventory is $ {:,.2f}".format(grand_total_value))
  return

def read_data(name_of_file):
  # inventory_read = [ ['abc',2,10.00], ['ban',200,20.00]] # (create empty list to save data found in name_of_file)
  inventory_read = []
  # open the file (name_of_file)
  read_file = open(name_of_file, 'r')
  # for each will loop through the file one line at a time
  for line in read_file:
    # each line is returned as a single string (not a list)
    # print("line initially is ", line)
    # python splitline() breaks the string into data
    split_line = line.rsplit(", ", 3)
    # then it returns a list
    # print("split_line type is, ", type(split_line))
    # this list can then be appended to the main list
    inventory_read.append(split_line)
  # Close the file after reading
  read_file.close()
  # call the print function to handle the list of data
  print_data(inventory_read)
  return

def main():
  print("\n\tWelcome to the Inventory Management System")
  print("\tPlease select from an option below: ")
  # do what is needed to create: name_of_file = "author_data.txt"
  name_of_file = "clinton_data.txt"
  create_new = open(name_of_file, 'x') # x creates the file
  create_new.close()
  # Display Main Menu:
  not_three = 0
  while not_three != 3:
    print("\n\t\tOption 1) Enter a new item into inventory")
    print("\t\tOption 2) Print the items found in inventory")
    print("\t\tOption 3) Exit the System")
    not_three = int(input("\t\t>> "))
    if not_three == 1:
      write_data(name_of_file)
    elif not_three == 2:
      read_data(name_of_file)
    elif not_three != 3:
      print("\t\tInvalid entry found, Please select 1, 2 of 3")
  print("\n\tThank you for using the Inventory Management System")
  return

main()
