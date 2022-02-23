# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# test_account_10_clinton.py
# CIS-135 Python
# Homework Assignment #10 – Object ATM - Test Account Class

# Code Summary:

# Change-Log: No updates logged yet

class Account:
  def __init__(self, first_given, last_given, pin_given):
    self.first_name = first_given
    self.last_name = last_given
    self.balance = 100.00
    self.pin = pin_given
    return

  def set_first_name(self, first_given):
    self.first_name = first_given
    return

  def get_first_name(self):
    return self.first_name

  def set_last_name(self, last_given):
    self.last_name = last_given
    return

  def get_last_name(self):
    return self.last_name

  def set_balance(self, new_balance_given):
    self.balance = new_balance_given
    return

  def get_balance(self):
    return self.balance

  def set_pin(self, new_pin_given):
    self.pin = new_pin_given
    return

  def get_pin(self):
    return self.pin
