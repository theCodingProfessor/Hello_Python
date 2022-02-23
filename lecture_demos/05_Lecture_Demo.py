# Code Demo for 05 Lecture
# Working with Output in Python
# CIS 135 - Code Demo File

# # Sample Order of Expression Statements
# print("\nSample Order of Expression Statements")
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

# # Simple If Statement in Python
# print("\nEvaluating a sale (200) to determine the discount")
# sales = 200
# discount = 0.0
# if sales > 100:
#   discount = 0.10
# print("The sale amount is: ", sales)
# print("The discount is: ", discount)
# print("The total amount after the discount is: $", sales * (1 - discount))

# # Simple If Statement in Python
# print("\nEvaluating a string to determine a grade")
# grade = 'B+'
# if grade == 'B':
#   print("You’ve earned a B")
# else:
#   print("You’ve grade cannot B determined.")

# # Sample showing Multiple lines of code in a Python If Statement
# print("\nIf statements can have multiple lines of code")
# if sales > 100:
#   discount = 0.10
#   discountAmount = sales * discount
#   subtotal = sales - discountAmount
# print(subtotal)

# # Sample showing an else statement in a Python If Statement
# print("\nIf statements with else")
# if sales > 100:
#   discount = 0.10
# else:
#   discount = 0.05

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

# Sample Multiple Evaluation Statements
# print("\nSample Multiple Evaluation Statements")
# print("(4.2 >= 5.0) and (8 == (13 + 5))", (4.2 >= 5.0) and (8 == (13 + 5)))
# print("(4.2 >= 5.0) or (8 == (3 + 5))", (4.2 >= 5.0) or (8 == (3 + 5)))
# print("(-2 < 0) and (18 >= 10)", (-2 < 0) and (18 >= 10))
# print("(-2 > 0) or (18 <= 10)", (-2 > 0) or (18 <= 10))
# if (2 <= 2) and (3 < 2):
#   print("one side is true in an and statement")
# elif (2 >= 2) and (3 > 2):
#   print("both sides are true in an and statement")
#
# if (2 < 2) or (3 < 2):
#   print("one side is true in an or statement")
# elif (2 >= 2) or (3 > 2):
#   print("both sides are true in an or statement")

# # Sample not Statements in Python
# print("\nSample not Statements in Python")
# print("not(18==(10+8) is:", (not(18 == (10+8))))
# print("not(10 <= 20)) is:", not(10 <= 20))
# print("not(2 != 2)) is:", not(2 != 2))
# print("not(12.5 > 4.56)) is: ", not(12.5 > 4.56))
# print("(not(18 == (10 + 28))) is:", (not(18 == (10 + 28))))
# print("(not(-4>0)) is:", (not(-4>0)))
# print('(not("Cat"<"Dog")) is:',  (not("Cat"<"Dog")))

# # Sample showing an elif statement in a Python If Statement
# # NOTE Change value of grade to show each statement evaluating
# print("\nSample Code for Python if-elif-else Statement(s)")
# grade = 70
# if grade >= 90:
#   print("The grade received is: A")
# elif grade >= 80:
#   print("The grade received is: B")
# elif grade >= 70:
#   print("The grade received is: C")
# elif grade >= 60:
#   print("The grade received is: D")
# else:
#   print("The grade received is: F")

# # Multiple evaluation in Python
# # NOTE Change value of numGrade to show each statement evaluating
# print("\nSample Code for Python with Multiple Selection in if-elif-else Statement(s)")
# numGrade = 90
# if numGrade >= 80 and numGrade < 90:
#   print("B")
# elif numGrade >= 60 and numGrade < 70:
#   print("D")
# elif numGrade >= 70 and numGrade < 80:
#   print("C")
# elif numGrade >= 90:
#   print("A")
# else:
#   print("F")

# # Case Study from Week 6 Lecture Notes (temperatures)
# # Ask the user for a temperature. If the temperature is over 80, print
# # “hot”. If the temperature is 33 to 80, print “moderate”. If the
# # temperature is 32 or less, print “freezing”.
# temp_given = int(input("Please enter the temperature: "))
# if(temp_given > 80):
#   print("hot")
# elif(temp_given > 32):
#   if(temp_given > 50):
#     if(temp_given == 51):
#       print("temp is 51")
#     print("moderately warm")
#   else:
#     print("moderately cool")
# else:
#   print("freezing")

# # Week 6 Case Study for Printing a Diploma
# # Print a diploma for a student if the number of credits they have earned
# # is 60 or more, if their gpa is at least 2.0, and if they do not owe any fees.
# credits = 0.00
# gpa = 0.00
# fees = 0.00
# credits = int(input("Please enter credits earned: "))
# gpa = float(input("Please enter the gpa earned: "))
# fees = float(input("Please enter fees remaining too be paid: "))
# #print(credits, gpa, fees)
#
# if(credits >= 60):
#   if(gpa >= 2.0):
#     if(fees <= 0.00):
#       print("\nHere is your diploma.")
#     else:
#       print("\nYou still have fees to pay before you can get your diploma.")
#   else:
#     print("\nYour gpa is below the level for earning a diploma.")
# else:
#   print("\nYou have not earned the required 60 credits to earn a diploma.")

num1, num2, num3, lowest= 1,2,3,10

if (num1 < num2):
  lowest = num1
elif (num1 < num3):
  lowest = num1
if (num2 < num3):
  lowest = num2
print(lowest)

new_low = num1
if (num2 < new_low):
  new_low = num2
if (num3 < new_low):
  new_low = num3
print(new_low)
