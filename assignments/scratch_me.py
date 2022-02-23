# Copyright (C) 2021 Clinton Garwood
# MIT Open Source Initiative Approved License
# error_handling_clinton.py
# CIS-135 Python
# Assignment #26 Handling Errors in Python

# Create a Python script file (named error_handling.py) that demonstrates several
# kinds of errors including, syntax errors, file-hadling errors and logic errors.

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
  # to divide the numerator by zero) = a divide by zero error.
  x = 1/0
  return

# Rubric 1 Point:
# Create a function named runLogicError that attempts to divide a number by zero.
# The code might be simply for example (x = 1/0). This error will be allowed to
# run (and throw its error when called in the generateErrors() function, and the
# error will be properly handled when called in the handleErrors() function.
def runFileError():
  # This function defines an operating system error (in this case the
  # code tries to open a file which does not exist).
  with open('file_does_not_exist') as f:
    read_data = f.read()
  return

def generateErrors():
  runLogicError()
  runFileError()
  return

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
  finally:
    print('Finally all the errors are handled!')

#generateErrors()
handleErrors()
