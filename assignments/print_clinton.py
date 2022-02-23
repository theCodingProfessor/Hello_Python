# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# print_clinton.py
# CIS-135 Python
# Assignment #6

hw = "hello world"
countdown = 0.12345

print(hw)
print(countdown)
# print("The value of hw is hello world.")
# print("The value of hw is", hw)

# # Using the different methods for formatted printing
# print("The value of hw is", hw, "." )
# print("The value of hw is " + hw + "." )
# print(f'The value of hw is {hw}.')
# print("The value of hw is {}".format(hw)+".")
# print("The value of hw is %s." %(hw))

print("The value of countdown is 0.12345")

# print("The value of hw is ", hw)
#
# # Rough Draft of printing Values
# # Using + or commas
# # Using '%' (%s string, %d integer, %f float)
# name_string, format_name,f_name = "a","b","c"
# num_float, format_num,f_num = 0,1,2
# print("I am %s and I have the number %f " %(name_string, num_float))
# # Using.format
# print("I am {} and have the number {}".format(format_name, format_num))
# # Using f string
# message = f'I am {f_name} and have the number {f_num}  '
#
#
# Countdown Component
#print(message)
print("The value of countdown is ,", "{0:.5f}".format(countdown))
print("The value of countdown is ,", "{0:.4f}".format(countdown))
print("The value of countdown is ,", "{0:.3f}".format(countdown))
print("The value of countdown is ,", "{0:.2f}".format(countdown))
print("The value of countdown is ,", "{0:.1f}".format(countdown))
print("The value of countdown is ,", "{0:.0f}".format(countdown))

# Final Output
message_goal = f'hello world the value of countdown is 0.12'
print("%s the value of countdown is {0:.2}".format(countdown) % hw)
