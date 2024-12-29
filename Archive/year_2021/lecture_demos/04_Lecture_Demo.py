# Code Demo for 04 Lecture
# Working with Output in Python
# CIS 135 - Code Demo File


# Sample Truthie Statements
# print("Sample True False Statements")
# print(10 <= 20)
# print(2 != 2)
# print(12.5 > 4.56)

# # Sample Order of Expression Statements
# print("\nSample Order of Expression Statements")
# print("4*3-8<=(18+28)/(4-20) evaluates as:", 4*3-8<=(18+28)/(4-20))
# print("4*3-8<=18+28/4-20 evaluates as:", 4*3-8<=18+28/4-20)

# # Sample Truthie Statements (Python uses the double == sign
# # to test truthness of a statement
# print("\nEvaluating Numbers")
# num1 = 1
# num10 = 10
# print("\nnum1 = ", num1)
# print("num10 = ", num10)
# print("num1 == 20:", (num1 == 20))
# print("100 > num1:", (100 > num1))
# print("num1 < num2:", (num1 < num10))

# # Sample Python String Comparisons using Relational Operators
# print("\nEvaluating Various Characters")
# print("'@' < 'a' is:",('@' < 'a'))
# print("'M' >= 'a' is:",('M' >= 'a'))
# print("'a' == 'aa' is:",('a' == 'aa'))
# print("'hat' > 'haM' is:",('hat' > 'haM'))
# print("'T' == 't' is:",('T' == 't'))

# # More Python String Comparisons using Relational Operators
# # Shows first character of the string is what is actually compared
# print("\nEvaluating Cats and Dogs")
# print('"Cat" == "Cats" is: ',("Cat" == "Cats"))
# print('"Cat" < "Cat" is: ',("Cat" < "Cat"))
# print('"CAT" == "cat" is: ',("CAT" == "cat"))
# print('"Dog" > "Cat" is: ',("Dog" > "Cat"))
# print('"Cat" < "Cap" is: ',("Cat" < "Cap"))
# print('"Dog" > "D" is: ',("Dog" > "D"))

# # Are these conditions true or false?
# print("\nEvaluating String Names")
# playerName = 'Patrick'
# print("playerName == 'Pat' evaluates as: ", (playerName == 'Pat'))
# print("playerName > 'Pat' evaluates as: ", (playerName > 'Pat'))
# print("'Pat' <= playerName evaluates as: ", ('Pat' <= playerName))

# # Simple If Statement in Python
# print("\nEvaluating a sale (200) to determine the discount")
sales = 200
# discount = 0.0
# if sales > 100:
#   discount = 0.10
# print("The sale amount is: ", sales)
# print("The discount is: ", discount)
# print("The total amount after the discount is: ${:.2f}".format(sales * (1 - discount)))

# # Simple If Statement in Python
# print("\nEvaluating a string to determine a grade")
# grade = 'B-'
# if grade == 'B':
#   print("\tYou’ve earned a B")
#   print("\tGreat Work")
# else:
#   print("\tYou’re grade cannot B determined.")

# # Sample showing Multiple lines of code in a Python If Statement
# print("\nIf statements can have multiple lines of code")
# if sales > 100:
#   discount = 0.10
#   discountAmount = sales * discount
#   subtotal = sales - discountAmount
# else:
#   print("sales were less than 100")
#
# print("subtotal is $ {:.2f}".format(subtotal))

# # Sample showing an else statement in a Python If Statement
# print("\nIf statements with else")
# if sales > 100:
#   discount = 0.10
# else:
#   discount = 0.05
#
# # Sample showing else statement with multiple lines in a Python If Statement
# # NOTE change this_sale to 100, 200 to demonstrate else in action
# this_sale = 150
# if this_sale > 100:
#   discount = 0.10
#   discountAmount = this_sale * discount
#   subtotal = this_sale - discountAmount
# else:
#   discount = 0.05
#   discountAmount = this_sale * discount
#   subtotal = this_sale - discountAmount
# print("the Subtotal is: ", subtotal)
#
# # Sample showing an elif statement in a Python If Statement
# # print("\nIf statements with elif")
# # if sales < 100:
# #   discount = 0.05
# # elif sales >= 100
# #   discount = 0.10

# grade = 'a'
# if grade == 'a':
#   print("Your Grade is: ", grade)
# elif grade == 'b':
#   print("Your Grade is: ", grade)
# elif grade == 'c':
#   print("Your Grade is: ", grade)
# elif grade == 'd':
#   print("Your Grade is: ", grade)
# else:
#   print('Sorry You did not pass.')
#
# print("done with evaluation")
#


# Demo on Swap Values
num1 = 30
num2 = 20
if num1 < num2:
  print("num1 is less than num2")
elif num1 == num2:
  print("num1 and num2 are equal")
else:
  print("num1 is greater than num2")
  temp = num1
  num1 = num2
  print("num1 =", num1)
  num2 = temp
  print("num2 =", num2)


# Demo on Functions
# Function is module in code
# acts like a variable,
# is 're usable'
name = "clinton"
mynumber= 7
print(name, mynumber)
print(name)
name = "garwood"
mynumber += 1
print(mynumber)

# Data Bucket - reusable data: Nouns
my_variable = "single piece of data"
my_tuple = ('zero', 'or more', 'data')
my_list = [1,2,3,3,['a','b','c']]
my_set = {(1,2), (2,3), (2,3)}
my_dictionary = {'key': 1, "key2": 2}

# re usabe actions Verbs
print(tuple)
print(list)

# set up an action, and 'call it' run-it when we want to
# function (is a bucket, which can have data, and also actions)

# def return_data(incoming_value,update_value):
#   # how much code, as much as you need
#   print("inside function send_it_in", incoming_value)
#   incoming_value += update_value
#   print("inside function send_it_in", incoming_value)
#   return incoming_value, 31

def get_input():
  next_num = int(input("Please enter the next number: "))
  print("you entered", next_num)
  return next_num

next_num = 0
while next_num != 1:
  next_num = get_input()

# send_it_in = 20
# print("before function call send_it_in ", send_it_in)
# send_it_in, returned_data = return_data(send_it_in, 20)
# print("after function call send_it_in ", send_it_in)
# print(returned_data)

# two ways to return data in programming
# 1) pass by reference
# 2) pass by value -- All data in python is pass by value




