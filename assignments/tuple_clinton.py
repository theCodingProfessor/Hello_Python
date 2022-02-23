# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# tuple_clinton.py
# CIS-135 Python
# Assignment #15 Python Tuples (Data Container)

# Rubric: 1 Point
# a) Declare a tuple named binaryNumbers and populate it with the following data
# (do not use a loop) 1000,1001,1010,1011,1100,1101,1110,1111
# b) Print the value of binaryNumbers
binaryNumbers = (1000,1001,1010,1011,1100,1101,1110,1111)
print()
print(binaryNumbers)

# Rubric 1 point:
# a) Declare a tuple named countUp and populate it with the following data
# (do not use a loop) "one","two","three","four","five","six","seven","eight"
# b) Print the value of countUp
countUp = ("one","two","three","four","five","six","seven","eight")
print()
print(countUp)

# Rubric 1 point:
# Print out the first, third and last value(s) from binNumbers
print()
print("binaryNumbers first value =", binaryNumbers[0])
print("binaryNumbers third value =", binaryNumbers[2])
print("binaryNumbers last value =", binaryNumbers[-1])

# Rubric 1 point: Print out the fourth, sixth, and eighth value(s) from countUp
print()
print("countUp fourth value =", countUp[3])
print("countUp sixth value =", countUp[5])
print("countUp eighth value =", countUp[7])

# Extra point: unpack the second and third piece of data from
# count up, and print them to the screen.
bin_two, bin_three = binaryNumbers[1:3]
bin_min_two, bin_min_three = binaryNumbers[-7:-5]
print()
print(bin_two, bin_three)
print(bin_min_two, bin_min_three)