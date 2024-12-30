# Code Demo for 02 Lecture
# Introduction to Python and Working with Data
# CIS 135 - Code Demo File

# # A Python function definition named main
# def main():
#   print("Inside the main function.")
#   return
#
# # In order to work, the function must be called
# print("Outside the main function.")
# main()
#
# def myAwesomeFunction(num1):
#   print(num1)
#   return
# iam007 = "007"
# myAwesomeFunction(iam007)
#
# # Numeric Variable Declaration in Python
# number_one = 1
# numberTwo = 2
# NUMBERTHREE = 3
# NumberFour = 4
# five = 5

# # String Variable Declaration in Python
# my_first_string = "one"
# stringTwo = "two"
# THIRDSTRING = "three"
# strFORE = "four"
# High_Five = "hello world"

# An Input Statement without a prompt
# Please uncomment the line below to run
# input()

# An Input Statement with a string literal prompt
# Please uncomment the line below to run
# input("Please enter a word")

# An Input Statement with a string literal prompt that saves the input
# Please uncomment the line below to run
# my_name = input("Please enter a word: ")

# Taking in a string, and converting it to an integer value
# An Input Statement with a string literal prompt that asks for a number
# In python the input statement always takes a string. 'literal character info"
# To use numeric data, you must cast the input to a numeric type
# Please uncomment both lines below to run
# my_integer = int(input("Please enter an integer: "))
# print(my_integer)
# print(type(my_integer))

# In the example above, we have wrapped the my_integer variable inside of the
# type() function call. This reveals the data_type for that variable.

# Taking in a string, but casting it to a float
# Please uncomment both lines below to run
# my_float = float(input("Please enter an decimal number"))
# print(type(my_float))

# In the example above, we have wrapped the my_float variable inside of the
# type() function call. This reveals the data_type for that variable.

# # Simple Print Statements
#
# # Print a string literal
# print("hello world")
#
# # Print a number
# print(21)
#
# # Print a variable
# my_language = 'Python'
# print(my_language)
#
# # Print a string literal and a variable
# print("My favorite language is,", my_language)
#
# # Examples of variable names
# roomLength = 24
# student_count = 18
# quizOneAverage = 94.3
# monthlySalary = 2500.00
# negative_value = -10
# playername = "Jordan"
# class_name_number = "CIS 135"
# print(roomLength)
# print(student_count)
# print(quizOneAverage)
# print(monthlySalary)
# print(negative_value)
# print(playername)
# print(class_name_number)

#
# # Examples of Updating a Variable
# roomLength = 24
# student_count = student_count + 3
# quizOneAverage = 95
# monthlySalary = 2500.00 + 200
# negative_value = -10 * 2
# playername = "Jordan" + ", " + "Michael"
# class_name_number = "CIS 135" + "W01"
# print(roomLength)
# print(student_count)
# print(quizOneAverage)
# print(monthlySalary)
# print(negative_value)
# print(playername)
# print(class_name_number)
#
# # Addition, Multiplication, Subtraction, Division
# int_one = 1  # simple assignment
# int_two = 1 + int_one  # using addition
# int_three = (int_two + int_two) - int_one  # addition and subtraction
# int_four = int((int_two * 4) / int_two) # division (forces a float, cast to int)
# int_five = divmod(((int_two + int_three) * int_two),2) # MOD division in Python
# print(int_one)
# print(int_two)
# print(int_three)
# print(int_four)
# print(int_five)
#
#A simple program in Python
def updateInteger(num1,num2):
  sum = num1 + num2
  return sum

def getText():
  sometext = input("Type a string: ")
  return sometext

def simple_program():
  num1, intVariable = 0,0
  while num1 < 2:
    intVariable = updateInteger(num1,num1+1)
    num1+=1
  stringVariable = getText()
  print(f'String received was, {stringVariable}')
  print(f'Final value of integers is {intVariable}')
  return

simple_program()

