# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# from_pseudocode_clinton.py
# CIS-135 Python
# Homework Programming Assignment #2 (Part 1)

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
print("Hello user")
# Display "Welcome to the gas mileage app"
print("Welcome to the gas mileage app")
# Display "This app will calculate gas mileage and the cost to fill your tank with gas."
print("This app will calculate gas mileage and the cost to fill your tank with gas.")

# * Acquire Data *
# Display  "Please enter in the cost of a gallon of gas"
print("Please enter in the cost of a gallon of gas")
# INPUT    gas_cost_per_gallon = input-cost
gas_cost_per_gallon = float(input())
# Display  "Please enter how many gallons your tank holds"
print("Please enter how many gallons your tank holds")
# INPUT    tank_total_gallons = input-gallons
tank_total_gallons = int(input())
# Display  "Please enter vehicle distance per gallon"
print("Please enter vehicle distance per gallon")
# INPUT    distance_per_gallon = input-distance
distance_per_gallon = float(input())

# * Compute *
# cost_to_fill_tank = gas_cost_per_gallon * tank_total_gallons
cost_to_fill_tank = gas_cost_per_gallon * tank_total_gallons
# distance_per_tank = tank_total_gallons / distance_per_gallon
distance_per_tank = tank_total_gallons / distance_per_gallon

# * Display Result to User *
# Display "Thank you for the data"
print("Thank you for the data")
# Display "The cost of filling your tank is: ", cost_to_fill_tank
print("The cost of filling your tank is: $ ", cost_to_fill_tank)
# The cost_to_fill_tank should be displayed in US Dollars
# For example 10 dollars should display as    [   $ 10.00   ]
# Display "The total distance you can go on a tank of gas is, distance_per_tank"
print("The total distance you can go on a tank of gas is, ", distance_per_tank, "-miles")
# The distance_per_tank should be displayed in miles [   40-miles ]
# Display: Thank you for using the Gas Mileage App.
print("Thank you for using the Gas Mileage App.")
