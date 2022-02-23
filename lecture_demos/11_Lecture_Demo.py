# Code Demo for 11 Lecture
# Working with Python Functions
# CIS 135 - Code Demo File

# Example of a simple function
def example_one():
  # this does nothing
  return
example_one()

# Example of a simple function
name = "Python"
def example_two(name):
  # this prints the name0
  print(f'\nThe string {name} was received by example_two')
  return
example_two(name)

# Example of a simple function that accepts multiple pieces of information
def example_three(a,b,c):
  # this prints the name0
  print(f'\nThe strings "{a}", "{b}", and "{c}" were received by example_three')
  return

# We can call a function, passing in data as variables:
x, y, z = "Python", "is", "great"
example_three(x,y,z)

# We can call a function, passing in literal data as well (here string literals):
example_three("Python","is","amazing")

# Example Menu Function
def display_menu():
  print("\nWelcome to the Inventory Menu")
  print("1) Add to Inventory")
  print("2) Delete from Inventory")
  print("3) Display Inventory")
  print("4) Exit")
  print()
  input("Please make a choice: ")
  return
display_menu()

def print_error_message():
  print("\nInvalid option.")
  return
print_error_message()

# Single Variable Function called with data (literal) and data (variable name)
def display_price(price):
  print("\nThe price is :", price)
  return

display_price(20) # This shows calling the function with data (literal)
price = 21
display_price(price) # This shows calling the function with data (variable)


def display_results(sum, count):
  print("The sum is: ", sum)
  print("The count is: ", sum)
  return

display_results(21,10)
twenty_one, ten = 21, 10
display_results(twenty_one,ten)

# Function to input sales data by person
def enter_sale(sales_by_person):  # takes the dictionary as input
  salesperson_name = input("Please enter the sales person's name: ")
  cars_sold = int(input("Please enter the number of cars sold: "))
  sales_by_person[salesperson_name] = cars_sold
  return sales_by_person # returns the dictionary after update

def compute_average(sales_by_person):
  count = 0
  sales = 0
  for each in sales_by_person:
    count += 1
    sales += sales_by_person[each]
  average_sales = sales / count
  print(f'\t\tThe average sales for data entered so far is: {average_sales}')
  return

# Sample Code: Car Sales Input Main Menu
def main_menu():
  print("\nWelcome to the Car Sales Input Application")
  sales_by_person = {}  # dictionary where name='key' and sales=value
  user_selected = 0
  while user_selected != 3:
    print("\tMain Menu")
    print("\t\tEnter 1) Input Sales Data")
    print("\t\tEnter 2) Calculate and Print Average")
    print("\t\tEnter 3) Exit Program")
    user_selected = int(input("\nPlease make a selection: "))
    if user_selected == 1:
      enter_sale(sales_by_person)
    elif user_selected == 2:
      compute_average(sales_by_person)
  return

main_menu()



