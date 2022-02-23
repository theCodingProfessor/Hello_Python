# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_4_clinton.py
# CIS-135 Python
# Homework Assignment #4 - A Phone Sales Application

# Code Summary:
# A program that computes total charges for phones sold
# and displays the initial charge, the tax and the total
# charge for that phone. The program allows a user to
# enter multiple phone sales and at the end displays a
# total value of the phones, total sales tax collected,
# and total sales for that session.

# Resources of Students
# Syntax Help - Resources:
# https://www.w3schools.com/python/python_functions.asp
# https://www.w3schools.com/python/python_ref_functions.asp
# https://www.w3schools.com/python/ref_func_format.asp

# Python Reference - The Docs
# https://docs.python.org/3/library/functions.html
# https://docs.python.org/3/library/index.html
# https://docs.python.org/3/reference/index.html#reference-index
# https://docs.python.org/3/reference/compound_stmts.html#function-definitions

def sales_data_report(total_phones_price, total_sales_tax_collected, total_sales):
  # Variable Declaration Area
  price_of_phone = 0.00 # (float)
  sales_tax = 0.00 # (float)
  tax_rate = 0.07 # (float)
  this_sale = 0.00 # (float)

  # Prompt the user for the price of a phone
  price_of_phone = float(input("\n\tPlease enter in the price of the phone: "))
  # Compute sale tax: price_of_phone x tax_rate (.07)
  sales_tax = price_of_phone * tax_rate
  # Compute Total Sale  price_of_phone + sales_tax
  this_sale = price_of_phone + sales_tax

  # Individual Phone Data Display: Use the format() string function
  # For currency data, display a $ and two numbers following the decimal place
  print("\n\tPhone Sale Summary")
  print("\t\tPhone List Price:    ${:>10,.2f}".format(price_of_phone))
  print("\t\tSales Tax Collected: ${:>10,.2f}".format(sales_tax))
  print("\t\tTotal Sale Price:    ${:>10,.2f}\n".format(this_sale))

  # Update and return grand_total variables
  total_phones_price += price_of_phone
  total_sales_tax_collected += sales_tax
  total_sales += this_sale
  return total_phones_price, total_sales_tax_collected, total_sales

def main():
  # Welcome the user
  print("\nWelcome to the Phone Sales Application")
  print("\n\tThis applicaton takes in individual phone sales data")
  print("\tand prints out the grand totals for the day's sales.")
  # Variable Declaration Area
  total_phones_sold = 0 # (integer)
  total_phones_price = 0.00 # (float)
  total_sales_tax_collected = 0.00 # (float)
  total_sales = 0.00 # (float)
  get_phones = 1
  # Loop until there is no data
  print("\n\tData Collection Module:")
  while(get_phones == 1):
  # Ask user if there is phone data to enter
    get_phones = int(input("\tTo add a phone enter 1; or enter 2 to exit: "))
    if (get_phones == 1):
      # Call sales_loop function and catch total data on function return
      total_phones_price, total_sales_tax_collected, total_sales = sales_data_report(total_phones_price,total_sales_tax_collected,total_sales)
      # update total phones sold
      total_phones_sold += 1
    else:
      print("\tEnd of Data Collection")
  # Final Display: Use the format() string function
  # For currency data, display a $ and two numbers following the decimal place
  print("\n\tGrand Total Sales Summary:")
  print("\t\tTotal Phones Sold:       {:>10}".format(total_phones_sold))
  print("\t\tTotal Phone Prices:     ${:>10,.2f}".format(total_phones_price))
  print("\t\tTotal Sales Tax:        ${:>10,.2f}".format(total_sales_tax_collected))
  print("\t\tSales Grand Total:      ${:>10,.2f}".format(total_sales))
  # Thank the user
  print("\nThank you for using the Phone Sales Data App")
  return

main()
