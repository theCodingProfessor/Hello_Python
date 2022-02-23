# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# payroll_ap.py
# CIS-135 Python
# Case Study for Creating a Payroll Application

''' Questions for the Client
1) Should more than one user pay item be entered
   Include a loop
2) What are the print formatting rules
'''

# Introduction
# Create Payroll App
# Welcome the user
print("\nWelcome to the Payroll App")
# explain to the user what the app does
print("\nEnter in an employees name, their hourly wage,")
print("and hours worked to compute their pay.\n")

# Acquisition of Data
# Get from User = name
last_name = input("\tPlease enter the employees last name: ")
# casting transform data from one type into another type
# Get from User = hours (take this info in as a float)
hours_worked = float(input("\tPlease enter the number of hours this employee worked: "))
# Get from User = wage (take this info in as a float)
hourly_wage = float(input("\tPlease enter the employees hourly rate: "))
print("\tThank you.\n")

# Compute
wages_earned = hours_worked * hourly_wage

# Communicate with the user again
# Display on Screen: name,
print("\n\t\tFor the Employee: ", last_name.title())
# Display on Screen: hours
print("\t\tThe total hours worked were: ", hours_worked)
# Display on Screen: wage for employee
print(f'\t\tThe rate for {last_name.title()} is : {hourly_wage}')
# # Display on Screen: total for the paycheck
print("\t\tThe total wages earned for this period are: ${:,.2f}".format(wages_earned))

