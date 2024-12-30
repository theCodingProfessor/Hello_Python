# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# updated_application_clinton.py
# CIS-135 Python
# Homework Programming Assignment #2 (Part 2)

''' Updated application from HW assignment Part 1. This update makes changes and suggestions as follows:
1) Data Types declared for required variables
   Floats: gas_cost_per_gallon, distance_per_gallon, cost_to_fill_tank, distance_per_tank
   Integer: tank_total_gallons
2) Communicate Section needs re-wording and reformatting: Suggestions include:
   print("Hello and Welcome to the Gas Mileage App"
3) In the Acquire Data Section:
   A) Rewording, re-formatting and streamlined input statements are suggested
   B) Casting Data is requried in Python (input only takes in strings).
   All numeric data is re-cast to the float or int data types
4) Logic Error found in Compute Data Section
   Original Specification said:
     from # distance_per_tank = tank_total_gallons / distance_per_gallon
   This should have been a multiplication not a division
     to # distance_per_tank = tank_total_gallons * distance_per_gallon
5) Final Section needs re-wording and reformatting: Suggestions include:
    print("Thank you") - moved up to data acquisition section.
    output changed: print("\tThe estimated total distance you can travel on a full tank is {}-miles."...
'''

# * Create Containers for Data*
# Variable for Cost per Gallon:  gas_cost_per_gallon
gas_cost_per_gallon = 0.00
# Variable for Total Gallons for Tank:  tank_total_gallons
tank_total_gallons = 0
# Variable for Cost per Distance per Gallon:  distance_per_gallon
distance_per_gallon = 0.00
# Variable for Cost to Fill Tank:  cost_to_fill_tank
cost_to_fill_tank = 0.00
# Variable for Distance per Tank:  distance_per_tank
distance_per_tank = 0.00

# * Communicate with User *
# Display "Hello user"
# print("\n\tHello user")
# Display "Welcome to the gas mileage app"
print("\n\n\tHello and Welcome to the Gas Mileage App")
# Display "This app will calculate gas mileage and the cost to fill your tank with gas."
print("\tThis app will calculate gas mileage and the cost to fill your tank with gas.")

# * Acquire Data *
# Display  "Please enter in the cost of a gallon of gas"
# print("Please enter in the cost of a gallon of gas")
# INPUT    gas_cost_per_gallon = input-cost
# gas_cost_per_gallon = float(input())
gas_cost_per_gallon = float(input("\n\t\tPlease enter the cost for a gallon of gas: "))
# Display  "Please enter how many gallons your tank holds"
# print("Please enter how many gallons your tank holds")
# INPUT    tank_total_gallons = input-gallons
# tank_total_gallons = int(input())
tank_total_gallons = int(input("\t\tHow many gallons does the tank hold: "))
# Display  "Please enter vehicle distance per gallon"
# print("Please enter vehicle distance per gallon")
# INPUT    distance_per_gallon = input-distance
# distance_per_gallon = float(input())
distance_per_gallon = float(input("\t\tPlease enter the vehicle miles-per-gallon (mph) : "))
# Display "Thank you for the data"
print("\t\tThank you.")

# * Compute *
# cost_to_fill_tank = gas_cost_per_gallon * tank_total_gallons
cost_to_fill_tank = gas_cost_per_gallon * tank_total_gallons
# distance_per_tank = tank_total_gallons / distance_per_gallon
# old-incorrect version  distance_per_tank = tank_total_gallons / distance_per_gallon
distance_per_tank = tank_total_gallons * distance_per_gallon

# * Display Result to User *
# Display "The cost of filling your tank is: ", cost_to_fill_tank
print("\n\tThe cost of filling your tank is: $ {:.2f}".format(cost_to_fill_tank))
# The cost_to_fill_tank should be displayed in US Dollars
# For example 10 dollars should display as    [   $ 10.00   ]
# Display "The total distance you can go on a tank of gas is, distance_per_tank"
print("\tThe estimated total distance you can travel on a full tank is {}-miles.".format(int(distance_per_tank)))
# The distance_per_tank should be displayed in miles [   40-miles ]
# Display: Thank you for using the Gas Mileage App.
print("\n\tThank you for using the Gas Mileage App.")
