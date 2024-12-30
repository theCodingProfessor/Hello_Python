# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# random_clinton.py
# CIS-135 Python
# Assignment #19 Random Number Generation in Python

# include needed library
import random

# Rubric 1 Point:
# Create and call a function named randomSimple that uses the Python randint()
# function to pick a number from one to ten. Print the result to the screen.
def randomSimple():
  print("\n\tThe number selected by random.randint() is: ", random.randint(1, 10), "\n")
  return
randomSimple()

# Rubric 1 Point:
# Create and call a function named randomChoice that uses the Python random.choice()
# function inside a loop that picks a value from a list named getRandomItem
# with the values ["one", "two", "three", "four", "five"] five times. Print the
# results of each selection to the screen.
def randomChoice():
  getRandomItem = ["one", "two", "three", "four", "five"]
  x = 0
  while x < 5:
    print("\tThe number selected by random.choice() is:", random.choice(getRandomItem))
    x+=1
  return
randomChoice()

# Rubric 1 Point:
# Create and call a function named randomFloat which implements Pythons random.random()
# function, nested inside a loop, which will continuously pick a random
# number until a number is selected which is greater-than-or-equal-to .75 Save the
# value of each number less-than .75 selected into a Python list, and return the list
# to the caller once the loop has ended. Print the returned list to the screen.
def randomFloat():
  float_list = []
  new_float = 0.0
  while new_float <= .75:
    new_float = random.random()
    if new_float <= .75:
      float_list.append(new_float)
  return float_list
print("\nThe list returned by random.random() is:", randomFloat())

# Rubric 1 Point:
# Create and call an interactive function named randomDice that makes use of a Python
# random integer number function to simulate the roll of a dice. Each time the user
# decides to roll the dice, have the function generate a number between 1 and 6 (inclusive)
# save the results to a python dictionary. Display the data saved to the dictionary with each
# roll. Once the user decides to end the session, return the dictionary to the caller
# and display it's data.
def randomDice():
  roll_results = {}
  roll_label = "Dice Roll #"
  roll_number = 1
  print("\n\tWelcome to the Python Dice Roller")
  r_or_q = input("\tTo roll the dice enter r (for roll), or q (to quit) ")
  while r_or_q == 'r':
    this_label = roll_label + str(roll_number)
    this_roll = random.randint(1, 6)
    roll_results.update({this_label:this_roll})
    roll_number +=1
    r_or_q = input("\tTo roll the dice enter r (for roll), or q (to quit) ")
  return roll_results

print("\nThe results of all dice rolls are:", randomDice())
