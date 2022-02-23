# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# dictionary_clinton.py
# CIS-135 Python
# Assignment #17 Python Dictionaries

# Rubric 1 point:
# Declare (and subsequently print) a Python dictionary  data structure
# named to_twenty which contains the following data:
# "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
# "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
# "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
# "nineteen": 19, "twenty": 20,
to_twenty = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20 }
print(to_twenty)
print()

# Declare (and print) a Python tuple data structure named primes which contains the data:
# 1,2,3,5,7,9,11,13,17,19
primes = (2,3,5,7,11,13,17,19)
print(primes)
print()

# Rubric 1 point:
# Create a Python function named compare_primes (giving it both data structures), and
# use a loop to compare each item in the to_twenty dictionary against the primes tuple.
# For each comparison print if the number being evaluated is a prime number or not.
def compare_primes(primes,to_twenty):
  in_twenty = to_twenty.values()
  for each in in_twenty:
    if each in primes:
      print("Number", each, "is prime.")
    else:
      print("Number", each, "is not prime.")

# Properly call the function compare_primes
compare_primes(primes,to_twenty)

# Rubric 1 point:
# Create an empty Python Dictionary named primes_to_twenty. Create a function named
# copyPrimes that uses a loop to check each node of data in the to_twenty dictionary
# against the numbers listed in primes (see above). When a number is found to be
# prime, copy the item (both the key:value) from the to_twenty dictionary into
# primes_to_twenty. Properly call the copyPrimes function (passing in the proper data)
# and catching primes_to_twenty which needs to be returned by the function. Print
# primes_to_twenty after the function returns.
primes_to_twenty = {}
def copyPrimes(primes_to_twenty,primes,to_twenty):
  for k,v in to_twenty.items():
    if v in primes:
      primes_to_twenty.update({k: v})
  return primes_to_twenty

primes_to_twenty = copyPrimes(primes_to_twenty,primes,to_twenty)
print()
print("The prime numbers to twenty are:", primes_to_twenty)
