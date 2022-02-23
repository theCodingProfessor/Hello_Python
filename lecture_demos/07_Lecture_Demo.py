# Code Demo for 07 Lecture
# Working with Repetition as Loops in Python
# CIS 135 - Code Demo File


# Initial Data from 06 Lecture is inlcuded (and commented out).
# Please search for START_07 to find the new code for the 2nd part of
# (or lecture 7) Lecture

# # Sample Variable Declaration
# userReply = "YES"
# inputData = -99
# counter = 10
# # Sample Comparisons
# print('True/False userReply == "YES")', userReply == "YES")
# print('True/False inputData != -99)', inputData != -99)
# print('True/False counter < 10)', counter < 10)
#
# # Sample data for Loop demos
# python_string_list = ["Chevy", "Ford", "Honda", "Ferrari", "Quit"]
# python_number_list = [100, 65, 82, 96, -99]
# loopControlVariable = 0
# count = 0
#
# # Simple While-True loop in Python
# print()
# count = 0
# while count < 10:
#   print(count)
#   count = count + 1
#
# # Simple While-False (not true) loop in Python
# num = input("\nInput zero to begin: ")
# while num != -1:
#   print("\t", num)
#   num = int(input("\tInput -1 to quit"))
#
# # NOTE the \t is a tab character which will indent output by four spaces
# # These are used by convention (not a rule) to show the 'loop output' as
# # a contrast to the regular run of code.
# print("\nWhile the loop control variable is less than five, print ")
# print("The value of the loopControlVariable, and then value of count ")
# while loopControlVariable < 10:
#   loopControlVariable = loopControlVariable + 1
#   count = count + 1
#   print("\tloopControlVariable = ", loopControlVariable)
#   print("\tcount = ", count)
#
#
# # Count up Loop which increments a number from 10 to 0
# # This shows the += syntax in python, which is equilavent to bottom_up = bottom_up + 1
# print("This while loop will count upwards from 0 to 10")
# bottom_up = 0
# while bottom_up < 11:
#   print("\tCount up from zero at: ", bottom_up)
#   bottom_up += 1
#   #bottom_up = bottom_up + 1
#
# # Countdown Loop which decrements a number from 10 to 0
# # Count up Loop which increments a number from 10 to 0
# # This shows the += syntax in python, which is equilavent to bottom_up = bottom_up + 1
# print("\nThis while loop will count downwards from 10 to 0")
# top_down = 10
# while top_down > -1:
#   print("\tCount down from 10 at: ", top_down)
#   top_down -= 1
#   #top_down = top_down - 1
#
#
# # Details the ability to have multiple control variables and counters
# print("\nThe loopControlVariable starts at zero and is increased to 10.")
# print("The multiplier variable is multiplied by two with each loop.")
# print("The shows using more than one variable in a while loop.")
# loopControlVariable = 0
# multiplier = 1
# while loopControlVariable < 10:
#   loopControlVariable += 1
#   multiplier = multiplier * 2
#   print("\tloopControlVariable = ", loopControlVariable)
#   print("\tmultiplier = ", multiplier)
#
# # Demonstrates off-by one in counting from 1 - 10
# print("\nPython For Loop prints 1-10, but is off-by one")
# print("This is due to the range() function starting its count at zero")
# print("This range = range(0,10)")
# for count in range(10):
#   print("\tRow ", count)
#
# # Updates off-by one in counting from 1 - 10
# # Proper 1 - 10 is printed
# print("\nPython For Loop printing what we want '1-10' without off-by one error")
# print("We handle this by starting the range() count at 1 and ending at 11")
# print("This range = range(1,11)")
# for count in range(1,11):
#   print("\tRow ", count)


# START_07
# START_07
# START_07

# # Simple Python While Loop
# print("\nSimple Python While loop counts from 0 to 5")
# count = 0
# while count < 6:
#   print("\t", count)
#   count += 1
#
# # Simple Python FOR Loop
# # print("\nPython For Loop printing what we want '1-10' without off-by one error")
# # Simple Loop:
# print("\nSimple Python While loop counts from 0 to 5")
# for each in range(0,6):
#   print("\t", each)
#
# # Lecture Demo, updating the sum
# # Here two variables are declared on the same line
# print("\nSimple Python while loop that sums input values")
# sum, new_score = 0, 0
# # While score is not the sentinel value
# while new_score != -99:
#   # Add score to sum
#   # consider why sum is updated before input is requested.
#   # what would happen if it was updated after input was received?
#   sum += new_score
#   # Get a score; Keep in mind we must cast the string recieved by input
#   # into an integer value; thus int(input())
#   new_score = int(input("\tPlease enter a score (enter -99 to exit): "))
# print("\t\tThe SUM of all input is:", sum)
#
#
# # Lecture Demo, asking a user for 'yes', 'y', or YES
# # This demo shows that even when the user says no to more data, it still
# # asks for a score. How would you fix this? Use a nested IF (see example that follows this)
# print("\nRequesting Input Yes with an input statement")
# sum, new_score, more_data = 0, 0, 'y'
# # While more_data is is equal to 'y'
# while more_data == 'y':
#   sum += new_score
#   # Ask user if they would like to enter a score
#   # DO NOT cast this input() to an integer value
#   more_data = input("\tTo enter a score type 'y' (for yes): ")
#   # Get the score data. Cast this string recieved to an int(input())
#   new_score = int(input("\tPlease enter a score: "))
# print("\t\tThe SUM of all input is:", sum)
#
# # Lecture Demo, asking a user for 'yes', 'y', or YES
# # This demo fixes the extra score problem from above
# print("\nRequesting Input Yes with an input statement")
# sum, new_score, more_data = 0, 0, 'y'
# # While more_data is is equal to 'y'
# while more_data == 'y':
#   sum += new_score
#   # Ask user if they would like to enter a score
#   # DO NOT cast this input() to an integer value
#   more_data = input("\tTo enter a score type 'y' (for yes): ")
#   # Get the score data. Cast this string recieved to an int(input())
#   if more_data == 'y':
#     new_score = int(input("\tPlease enter a score: "))
# print("\t\tThe SUM of all input is:", sum)


# Lecture Demo shows use of built in string function upper() to convert user
# input to "UPPER CASE "Y" character
print("\nRequesting Input Yes with an input statement")
sum, new_score, more_data = 0, 0, 'Y'
# While more_data is is equal to 'y'
while more_data == 'Y':
  sum += new_score
  # Ask user if they would like to enter a score
  # DO NOT cast this input() to an integer value
  more_data = input("\tTo enter a score type 'y' (for yes): ").upper()
  # Get the score data. Cast this string recieved to an int(input())
  if more_data == 'Y':
    new_score = int(input("\tPlease enter a score: "))
print("\t\tThe SUM of all input is:", sum)

# Lecture Demo shows use of built in string function lower() to convert user
# input to "lower case "y" character
print("\nRequesting Input Yes with an input statement")
sum, new_score, more_data = 0, 0, 'y'
# While more_data is is equal to 'y'
while more_data == 'y':
  sum += new_score
  # Ask user if they would like to enter a score
  # DO NOT cast this input() to an integer value
  more_data = input("\tTo enter a score type 'y' (for yes): ").lower()
  # Get the score data. Cast this string recieved to an int(input())
  if more_data == 'y':
    new_score = int(input("\tPlease enter a score: "))
print("\t\tThe SUM of all input is:", sum)
