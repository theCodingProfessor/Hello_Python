# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# error_handling_clinton.py
# CIS-135 Python
# Assignment #26 Handling Errors in Python

# Create a Python script file (named error_handling.py) that demonstrates several
# kinds of errors including, syntax errors, file-handling errors and logic errors.

# Rubric 1 Point:
# Create a function named causeSyntaxError with a mangled print statement. The
# intention of this function is to deliberately cause a syntax error. Do not
# call the function anywhere in the script, but notice when you do run the script
# that even though the code is 'unreachable' the file will still fail to run.
def causeSyntaxError():
  # Syntax errors even if they called or reached (for example this error in a
  # function which is never called. Syntax errors are parsing errors, and parsing
  # is done before run-time. Syntax cannot be caught with a try-catch blocks either.
  # They must be eliminated before a script is offered to the Python intepreter.
  # Uncomment the mangled print statement below to see how a syntax error looks.
  # print "This Syntax Error is included as an example."
  return

# Rubric 1 Point:
# Create a function named runLogicError that attempts to divide a number by zero.
# The code might be simply for example (x = 1/0). This error will be allowed to
# run (and throw its error when called in the generateErrors() function, and the
# error will be properly handled when called in the handleErrors() function.
def runLogicError():
  # This function defines a logic error (in this case the code tries
  # to divide the numerator by zero) or a divide by zero error.
  x = 1/0
  return

# Rubric 1 Point:
# Create a function named runFileError that attempts to open a file which does
# not exist. Use an 'with open()' statement as described in exercise 25. This error
# will be allowed to run (and throw its error when called in the generateErrors()
# function, and the error will be properly handled when called in the handleErrors()
# function.
def runFileError():
  # This function defines an operating system error (in this case the code tries to
  # open a file which does not exist). The error can be caught by either OSError or
  # FileNotFoundError.
  with open('file_does_not_exist', 'r') as f:
    read_data = f.read()
  return

# Rubric 1 Point:
# Create a function named generateErrors that first calls runLogicError() and then
# calls runFileError(). Do not do any error handling, but rather study the error(s)
# that are thrown. You will have to comment out the runLogicError() function call
# in order to actually see the runFileError() error message.
def generateErrors():
  runLogicError()
  runFileError()
  return

# Rubric 1 Point:
# Create a function named handleErrors that uses try-catch blocks to properly
# handle the errors thrown by runLogicError() and runFileError(). In the code
# use a 'finally' block which prints out a final message after all the errors
# have been properly handled. Make sure to call handleErrors and study the output.
def handleErrors():
  # A try-catch block can be used to catch logic errors like this:
  try:
    try:
      runLogicError()
    except ZeroDivisionError as err:
      print('Now handling:', err)
    try:
      runFileError()
    except (OSError, FileNotFoundError) as err:
      print('Now handling:', err)
  # The finally block always runs even if no errors are found/caught.
  finally:
    print('Finally all the errors are handled!')
  return

#generateErrors()
handleErrors()