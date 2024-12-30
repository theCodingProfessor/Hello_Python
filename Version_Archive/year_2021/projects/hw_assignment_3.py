# Sample Code For Assignment #3
# Printing Formatted Data in Python

# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_3.py
# CIS-135 Python

# Coding_Resources:
# https://www.w3schools.com/python/ref_string_format.asp
# https://www.w3schools.com/python/python_string_formatting.asp
# https://www.w3schools.com/python/python_strings.asp
# http://stackoverflow.com/questions/21208376/ddg#21208495
# https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents


# RAW DATA
# Category Type Count Total Value
# Adapter Bluetooth Mobile 284 7,097.16
# Network Switch Cisco 103 10,298.97
# Laptop computer Chromebook 7 2,100.00
# SSD External 83 9,877.00

# What is a Header?
# What is table data?

# Header Data
# Category Type Count Total Value

# Table Data
# Adapter Bluetooth Mobile 284 7,097.16
# Network Switch Cisco 103 10,298.97
# Laptop computer Chromebook 7 2,100.00
# SSD External 83 9,877.00

# When we think of a table, we think of rows and columns that are
# all the same width:
#|____|____|____|____|____|
#|____|____|____|____|____|
#|____|____|____|____|____|

# Sometimes, though, we need more/less width to accommodate data
# of different lengths
#|__________|____|_________|_|__|
#|__________|____|_________|_|__|
#|__________|____|_________|_|__|
#|__________|____|_________|_|__|

# # As we can see, not all data is the same length, and columns do not
# # always naturally align:
# print("\nCategory Type Count Total Value")
# print("Adapter Bluetooth Mobile 284 7,097.16")

# # Even using tabs between data items does not always do the trick.
# print("\nCategory\t\t\tType\t\t\tCount\t\t\tTotal\t\t\tValue")
# print("Adapter Bluetooth\t\t\tMobile\t\t\t284\t\t\t7,097.16")

# # A more robust solution is needed.

# # We can turn to a formatted print statement to help us out:
# # A formatted print statement is a string which we can use
# # to insert data into, when we want to.
# simple_format = "\nData is inserted where the curly braces appear: {}"

# # To use a formatted print statement we use the print statement and a
# # call to the .format() method. Inside the (parenthesis) of the formatted
# # print statement we insert the variable or data.
# print(simple_format)
# print(simple_format.format("Hello World"))

# # We can also do this with a variable
# hs = "Hello Student"
# print(simple_format.format(hs))


# # The {} can be anywhere in the statement:
# what_to_do = "\nLearning {} is fun."
# language_name = "Python"
# print(what_to_do.format(language_name))

# # We can also insert and format numbers using the Print statement
#pi_is = "\nThe first ten digits of pi are: {}"
# pi_to_ten = 3.1415926535
#print(pi_is.format(pi_to_ten))

# # We can reuse statements as many times as we like.
# pi_to_four = "\nThe first four digits of pi are: {:.5}"
# print(pi_to_four.format(pi_to_ten))

# # We can also add padding to our formatted print statements.
# print()
# pi_dec_five = "{:6.5} are the first five decimals of pi."
# pi_dec_four = "{:6.4} are the first four decimals of pi."
# pi_dec_three = "{:6.3} are the first three decimals of pi."
# pi_dec_two = "{:6.2} are the first two decimals of pi."
#
# print(pi_dec_five.format(pi_to_ten))
# print(pi_dec_four.format(pi_to_ten))
# print(pi_dec_three.format(pi_to_ten))
# print(pi_dec_two.format(pi_to_ten))

# # And can also add alignment to our formatted print statements.
# print()
# pi_dec_five = "{:<6.5} are the first five decimals of pi."
# pi_dec_four = "{:<6.4} are the first four decimals of pi."
# pi_dec_three = "{:<6.3} are the first three decimals of pi."
# pi_dec_two = "{:<6.2} are the first two decimals of pi."
# print(pi_dec_five.format(pi_to_ten))
# print(pi_dec_four.format(pi_to_ten))
# print(pi_dec_three.format(pi_to_ten))
# print(pi_dec_two.format(pi_to_ten))

# # Raw Data as Tuples
# title = ("Category", "Type", "Count", "Total Value")
# row1 = ("Adapter","Bluetooth","Mobile","284","7097.16")
# row2 = ("Network Switch","Cisco","103","10,298.97")
# row3 = ("Laptop computer","Chromebook","7","2100")
# row4 = ("SSD","External","83","9877")
#
# # # RAW DATA as List
# header = ["Category", "Type", "Count", "Total Value"]
# r1 = ["Adapter","Bluetooth Mobile","284","7,097.16"]
# r2 = ["Network Switch","Cisco","103","10,298.97"]
# r3 = ["Laptop computer","Chromebook","7","2,100.00"]
# r4 = ["SSD","External","83","9,877.00"]

# # Given the raw data, we look for the longest of the strings:
# # Laptop Computer = 17 characters so 20 characters would be a good length for column 1
# # Bluetooth Mobile = 16 characters so 20 would be a good length for col 2
# # Count = 5 characters so 10 would be a good length for col 3
# # Total Value = 11 characters so 15 would be a good length for col 4
# # Setup the placeholders: {:20}{:20}{:10}{:15}

# # Create the placeholder string: {:20}{:15}{:9}{:15}
# # When we print from a tuple or a list (data is in this format above),
# # we need to adjust the placeholder by adding an integer to the left
# # of the colon in each placeholder.
# # for example to print the first piece of data we use {0:20}
# # to print the second piece of data we use {1:15} etc.
#
# print_string = "{0:20}{1:20}{2:>10}{3:>15}"
#
# # # Call (use) the print string to print out a sample of the data:
# print()
# print(print_string.format(header[0],header[1],header[2],header[3]))
# print(print_string.format(r1[0],r1[1],r1[2],r1[3]))
# print(print_string.format(r2[0],r2[1],r2[2],r2[3]))
# print(print_string.format(r3[0],r3[1],r3[2],r3[3]))
# print(print_string.format(r4[0],r4[1],r4[2],r4[3]))
#
#
# Notes on Homework Assignment #3

myInt = 10
myString = "Clinton"
chevy = "Cheverolet      Silverado       586,675      $ 28,595.00"
chevy = "Cheverolet      Equinox       1,270,994      $ 25,000.00"

# # Variable = one named space in memory
# # Variable that can hold mulipiple piece of information.
# my_variable = 10 # 'string' double/flaot   # First container
# my_tuple = 10,20,30,40,50,60,70          # Second type of container
# my_tuple = (10,10,10,20,30,40,50,60,70,80)     # Cannot update a tuple, using same name = new
# my_list = [40,20,35,"twenty",10.2,10.11,["clinton","garwood",[1,2,3,4]]]  # Third type of data continer
# my_set = {30,100,20,30,30,30,30} # fourth data container
# my_dictionary = {'first_name': 'Clinton', 'last_name': 'Garwood', 'id': 36643.00 } # fifth type
# print(my_list)

# # RAW DATA:
# Chevrolet	Silverado	586675	28595
# Chevrolet	Equinox	270994	25000
# Ford	F-Series	787422	30635
# GMC	Sierra	253016	29695
# Honda	CR-V	333502	26525
# Honda	Civic	261225	22000
# Lamborghini	Huracan	1095	208571
# Toyota	RAV4	430387	27325
# Toyota	Camry	29434825965

# r1 = ["Chevrolet", "Silverado", 586675, 28595]
# r2 = ["Chevrolet", "Equinox", 270994, 25000]
# r3 = ["Ford", "F-Series", 787422, 30635]
# r4 = ["GMC", "Sierra", 253016,29695]
# r5 = ["Honda", "CR-V", 333502,26525]
# r6 = ["Honda", "Civic", 261225,22000]
# r7 = ["Lamborghini", "Huracan",1095,208571]
# r8 = ["Toyota", "RAV4", 430387,27325]
# r9 = ["Toyota", "Camry", 294348,25965]

# # # Example of printing raw data as a string literal in a print statement:
# print("\nChevrolet    Silverado    586675    28595")
# print("Chevrolet    Equinox    270994    25000")
# print("Ford    F-Series    787422    30635")
# print("GMC    Sierra    253016    29695")
# print("Problems here as rows are not lined up and numbers are not formatted\n")

# # # Printing raw data using some basic formatting a print statement :
# # # This shows using a tab between each value
# # # Chevrolet	Silverado	586675	28595
# print("\n\tChevrolet\tSilverado\t586675\t28595")
# print("\tChevrolet\tEquinox\t270994\t25000")
# print("\tFord\tF-Series\t787422\t30635")
# print("\tGMC\tSierra\t253016\t29695")
# print("Problems continue with row alignment and numbers formatting\n")
#
# print(r1)
# print(r2)
# print(r3)
# print(r4)
# print(r5)
# print(r6)
# print(r7)
# print(r8)
# print(r9)
# # More on printing simple strings:
# print("Working with raw data creates problems, both with")
# print("handling the data initially, and more importantly when")
# print("we want to update or change data based on program input")

# # Using data buckets to control the data.
# # Python has many differnt kinds of buckets for data.
# # You have already seen variables
# number_10 = 10
#
# # What if we want to store two pieces of data in a single container?
# # A tuple can be used to store more than one piece of data.
# # https://www.w3schools.com/python/python_tuples.asp
# # https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple
# my_tuple = (10, 20)
# one_to_ten_tuple = (1,2,3,4,5,6,7,8,9,10)
# # We can store as many items (in an ordered fashion) as we want in a tuple.
# # Printing tuples work just like variables
# print(my_tuple)
# print(one_to_ten_tuple)
#
# # Python Lists:
# # https://www.w3schools.com/python/python_lists.asp
# # https://docs.python.org/3/library/stdtypes.html?#list
# # Another bucket we can use to store multiple pieces of (ordered data) in
# # Python is called a List.
# my_list = [10, 20]
# one_to_ten_list = [1,2,3,4,5,6,7,8,9,10]
# # We can store as many items (in an ordered fashion) as we want in a list.
# # and printing lists works just like variables
# print(my_list)
# print(one_to_ten_list)

# #
# print("\n\tIt is better, down the road, to use Lists that tuples")
# print("\tLists are mutable -- because can be changed and updated.\n")
#
# # How would our raw data look if it were formatted as a tuple:
# # Can format Data as Tuples:
ti = ("Car Make", "Car Model", "Units Sold", "Starting Price")
sep = ["--------", "---------", "----------", "--------------"]
#
# # How would our raw data look if it were formatted as a list:
# # Can Format data as Lists
cs = ["Chevrolet", "Silverado", 586675, 28595]
ce = ["Chevrolet", "Equinox", 270994, 25000.00]
fo = ["Ford", "F-Series", 787422, 30635]
gm = ["GMC", "Sierra", 253016, 29695]
hv = ["Honda", "CR-V", 333502, 26525]
hc = ["Honda", "Civic", 261225, 22000]
lh = ["Lamborghini", "Huracan", 1095, 208571]
tr = ["Toyota", "RAV4", 430387, 27325]
tc = ["Toyota", "Camry", 294348, 25965]

# # Once our raw data is in a proper bucket, we can use a formatted print
# # string to handle the formatting fine-tuning, and also to add symbols like
# # decimal points, and row padding and alignment.
#
# # A formatted print string literal, allows us to define how we want
# # our output to be displayed. Once the string is created, then we can simply
# # use that string and insert the new data which we want to display.
#
# # Formatted print string for the Header
# # Set up a print format string for the column headers
car = "ford"
car_title = "{0:<12} {1:<12}{2:>15}{3:>20}"
# # variable assignment "formatted statement"
# # within the formatted statement {} indicates a placeholder
# # here we see four placeholders {}{}{}{}
# # Inside the {placeholder} we define the style
# # { left-curly brace     int(tuple/list/position) colon position/formatting right-curly brace }
# # https://www.w3schools.com/python/python_string_formatting.asp
#
# # {0:12}  - means a placeholder that takes the first item in a tuple (0)
# #           and reserves 12 spaces for the data
#
# # {0:2}   - means a placeholder that takes the first item in a tuple (0)
# #           and reserves 2 spaces for the data

# # {1:.2}  - means a placeholder that takes the second item in a tuple (1)
# #           and displays the data as a float (decimal) with two degrees of precision

# # {0:<10}  - means a placeholder that takes the first item in a tuple (0)
# #           reserves 10 spaces for the data, and aligns it to the left <

# # {0:>5.2}  - means a placeholder that takes the first item in a tuple (0)
# #            reserves 5 spaces for data, right-aligns it, and displays it with
# #            a decimal point and two degrees of precision

# # Formatted print string for the Data
# # Set up a print format string for the car data
car_data = "{0:12} {1:12}{2:>15,}{3:7>}{4:15,.2f}"

# # sometimes to get the format we want, we need to insert spaces "literal space"
# # between the placeholders. We see this above between position 3 and 4
# # also notice we have a dollar sign included as well.
#
# Print out the data for the header:
print(car_title.format(ti[0],ti[1],ti[2],ti[3]))
print(car_title.format(sep[0],sep[1],sep[2],sep[3]))

# Print out the data for each car:
print(car_data.format(cs[0],cs[1],cs[2],'$',cs[3]))
print(car_data.format(ce[0],ce[1],ce[2],'$',ce[3]))
print(car_data.format(fo[0],fo[1],fo[2],'$',fo[3]))
# print(car_data.format(gm[0],gm[1],gm[2],gm[3]))
# print(car_data.format(hv[0],hv[1],hv[2],hv[3]))
# print(car_data.format(hc[0],hc[1],hc[2],hc[3]))
# print(car_data.format(lh[0],lh[1],lh[2],lh[3]))
# print(car_data.format(tr[0],tr[1],tr[2],tr[3]))
# print(car_data.format(tc[0],tc[1],tc[2],tc[3]))

