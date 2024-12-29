# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# hw_assignment_10_clinton.py
# CIS-135 Python
# Homework Assignment #10 – Object ATM

from new_folder.account import Account

# Code Summary: Menu-driven program that simulates an ATM
# (Automatic Teller Machine) interface. A user of the application
# can set up an account, make deposits, withdraws, and
# check their account balance.

# Change-Log: Adding Get Balance, Deposit and Withdraw
# functions to app code. Relies on getters and setters for
# data from the class file.

# Account Setup Function
def setup_function():
  first_name = input("\n\t\tPlease enter a first name ")
  last_name = input("\t\tPlease enter a last name ")
  the_pin = input("\t\tPlease enter a pin security code ")
  # initalize an obect from the account_class to save
  # first name, save last name and balance = 100.00
  new_account = Account(first_name,last_name,the_pin)
  # return account_object
  print("\n\t\tNew Account has been created for:")
  print("\t\t", new_account.get_last_name(), ",", new_account.get_first_name())
  print("\t\t Account Balance: ", new_account.get_balance())
  return new_account

def display_balance(this_account):
  print("\n\t\tAccount Balance Option Selected")
  print("\t\tThe Balance for this account is: ${:,.2f}".format(this_account.get_balance()))
  return

def deposit_funds(this_account):
  print("\n\t\tAccount Deposit Option Selected")
  deposit_amount = float(input("\t\tFund amount to deposit: "))
  new_balance = deposit_amount + this_account.get_balance()
  this_account.set_balance(new_balance)
  print("\t\tYour new account balance is: ${:,.2f}".format(this_account.get_balance()))
  return

def withdraw_funds(this_account):
  print("\n\t\tAccount Withdraw Option Selected")
  withdraw_amount = float(input("\t\tFund amount to withdraw: "))
  if this_account.get_balance() >= withdraw_amount:
    new_balance = this_account.get_balance() - withdraw_amount
    this_account.set_balance(new_balance)
    print("\t\tYour new account balance is: ${:,.2f}".format(this_account.get_balance()))
  else:
    print("\t\tInsufficient funds to handle this transaction")
    print("\t\tAccount balance is: ${:,.2f}".format(this_account.get_balance()))
  return

# Start Display Menu Function
def display_menu():
  print("\n\t\tPlease select an option")
  print("\t\tOption 1) Display Account Balance")
  print("\t\tOption 2) Make a Deposit")
  print("\t\tOption 3) Make a Withdraw")
  print("\t\tOption 4) Exit the App")
  return

# start main function
def main():
  print("\nWelcome to the Python Object ATM")
  # call setup_account function and catch this_account
  this_account = setup_function()
  # call display_menu function
  user_request = 0
  while user_request != 4 :
    display_menu()
    user_request = int(input("\t\t>> "))
    if user_request == 1:
      display_balance(this_account)
    elif user_request == 2:
      deposit_funds(this_account)
    elif user_request == 3:
      withdraw_funds(this_account)
    elif user_request != 4:
      print("\t\tInvalid data received. Please try again.")
  print("\nThank you for using the Python Object ATM")
  # end main function
  return

# call main function
main()