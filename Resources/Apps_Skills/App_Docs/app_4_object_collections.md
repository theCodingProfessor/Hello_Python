### Application 4: Manage Object Collections
**Topics:** Class and Objects, Collection Resources

<hr>

### 1. Objective
**Purpose:**  
- This assignment asks you to create an Object-Oriented app.
- Incorporate OOP principles including definitions of the Class(es), and storage of initialized objects in a collection (i.e., list or dictionary).
- Connect user interaction with the object collection (i.e., menu or user prompts).
- Develop your own app idea or use the provided examples to get started. 

**Pathway:**
1) Describe an Object-Oriented application using pseudocode or another type of design document.
2) Convey the logic of the application being proposed as the `specification`
3) Translate the `specification` into a Python application.

#### Object-Oriented Project Concepts:
Experimenting in a topic area of interest to you is encouraged (but not required).
Select a concept and define its design (algorithm) document before creating code.
-- New user registration (programming)
-- Agent traversal over a network (logistics, data science)
-- Spam Detector (IT, cybersecurity)
-- Unit Testing (dev-ops, programming)
-- Lift-and-Load data conversions (data science)

<hr>

### 2. Learning Outcomes

- **Design:** Create an object-oriented design document that includes class definitions, functions, and object storage.
- **Develop:** Implement the design into a Python program that uses object-oriented principles, including classes and collections.
- **Troubleshoot:** Identify and correct issues with object interactions, methods, and collections, documenting them in a Change Log.

<hr>

### 3. Assignment Instructions

**Part 1-1: Initialize a Design Document**  
- **Working Title:** Provide a meaningful title for your app.
- **Author Information:** Include your name.
- **Description:** Write a short description of the algorithm or app.
- **Representation:** UML, Pseudocode, and other design documents as needed.

**Part 1-2: Define the Algorithm as Pseudocode
- Declare a program START.
- For each Class in the Application:
    - Declare a START_CLASS_NAME.
    - Define attributes and methods.
    - Declare an END_CLASS_NAME.
- For each Function in the Application (user prompts or menu options):
    - Declare a START_FUNCTION_NAME.
    - Define steps as needed.
    - Declare an END_FUNCTION_NAME.
- Declare a program STOP.
- **Address Object Collection:** Decide how you will store the objects (in a list or dictionary) and describe how they will be accessed and manipulated through the program, likely a data structure in main(). 

**Part 1-2: Define the Class Design as Pseudocode
- **Class Design:** Define each class, its attributes, and methods. Use diagrams, pseudocode, or text-based explanations.

**Part 1-3: Define the Class Design as UML (Unified Modeling Language) Object 
- **Class Design:** Namespace, attributes, and methods. Use line art box.

**Part 2: Create the Application**  
- **Translation:** Convert the design document into a working Python app.
- **Change Log:** If you encounter logic errors during coding (steps out of order, missing loops), make the necessary corrections in the code. Document these changes in a multi-line comment section titled **"Change Log"** at the top of your code.

<hr>

### 4. Submission Requirements

- **Design Document:** Submit a design document. Markdown (.md), PDF (.pdf) or MS Word (.docx) document types.
- **Python Source Code Files:** Submit a Python file (.py) for the driver program and any additional class files. Ensure the files are structured so that the driver program can import and use the class files.

<hr>

### 5. Success Criteria
- **Design Document:**  
  - The required header is present
  - Visual indentation of functions and code logic in pseudocode.
  - Visual separation of each function in the pseudocode document

**Python Code:**
- Correct implementation of OOP principles, including class design and object interaction.
- Functionality and correctness of methods and object collection handling.

- **Change Log:**  
  - Accurate and clear documentation of any issues encountered and the changes made.

<hr>

### 6. Samples

**Design Document:**

** Tech Terms Dictionary (as class Terms) App**  
- **App Type:** Knowledge, Programming
- **Author:** Clinton Garwood  
- **August 2024** 
- **Description:** This application allows a user to add or lookup a term-definition pair by entering a keyword. Using a 'Terms' class the `pickle` dictionary provides permanent storage. 
-  Algorithm Representation: Pseudocode
	

**Class File `Terms` Representation as UML:**
### Class File: 

``` plaintext
 +--------------------------------- Namespace +
 |           Terms                            |
 +-------------------------------- Attributes + 
 | - term_name: String                        |   
 | - definition: List[String]                 |   
 +----------------------------------- Methods +
 | + __init__(term_keyword: String,           |
              as_defined: String = "unknown") |
 | + set_term_name(term_name: String): void   |
 | + set_definition(new_define: String): void |
 | + get_term_name(): String                  |
 | + get_definition(): List[String]           |
 +--------------------------------------------+

```
Class Name: `Terms` 

Attributes:
`term_name` is a label with private attribute (-) for type String.

`definition` is the full-text with private attribute (-) for type List[String].

Methods:
`__init__` constructor initializes the attributes. The default value as_defined is shown.

`set_term_name` and `set_definition` are public methods (+) and don't return values (void).

`get_term_name` and `get_definition` are public methods that return the corresponding attribute types (String and List[String]).


**Algorithm Representation as Pseudocode:**

```markdown
# Pseudocode for Technology Terms App

## START CLASS Terms
- **Attributes**:
  - term_name: string
  - definition: list of strings
  
- **Methods**:
  START METHOD __init__(term_keyword, as_defined)
    SET term_name = term_keyword
    SET definition = [as_defined]
  END METHOD
  
  START METHOD set_term_name(term_name)
    SET self.term_name = term_name
  END METHOD
  
  START METHOD set_definition(new_define)
    APPEND new_define to self.definition
  END METHOD
  
  START METHOD get_term_name()
    RETURN self.term_name
  END METHOD
  
  START METHOD get_definition()
    RETURN self.definition
  END METHOD
END CLASS

## START FUNCTION terms_menu
PRINT "1) Lookup a Term"
PRINT "2) Add a Term"
PRINT "3) Update a Term"
PRINT "4) Exit"
RETURN
END FUNCTION

## START FUNCTION main
PRINT "\nTechnical Term Lookup App"
  CALL load_terms_dict('terms_dict.pkl') AND ASSIGN TO terms_dict
  
  WHILE True
    CALL terms_menu()
    CALL get_terms_choice() AND ASSIGN TO user_choice
  
    IF user_choice = '1'
      CALL get_term(terms_dict)
    ELSE IF user_choice = '2'
      CALL add_term(terms_dict)
    ELSE IF user_choice = '3'
      CALL update_term(terms_dict)
    ELSE IF user_choice = '4'
      CALL save_terms_dict(terms_dict, 'terms_dict.pkl')
      PRINT "\tExiting..."
      BREAK
    ELSE
      PRINT "\tInvalid choice. Please select again."
  END WHILE
END FUNCTION
``` 

``` plaintext 
START FUNCTION load_terms_dict(filename)
  IF file exists at filename
    OPEN filename in 'rb' mode AND ASSIGN to f
    LOAD pickled data from f AND ASSIGN to terms_dict
    PRINT "\tLoaded terms from", filename
  ELSE
    SET terms_dict = empty dictionary
    PRINT "\tNo existing data found. Starting fresh."
  RETURN terms_dict
END FUNCTION
``` 

``` plaintext 
START FUNCTION save_terms_dict(terms_dict, filename)
  OPEN filename in 'wb' mode AND ASSIGN to f
  PICKLE dump terms_dict into f
  PRINT "\tData saved to", filename
END FUNCTION
``` 

``` plaintext 
START FUNCTION get_terms_choice
  CALL INPUT("\tPlease select: ") AND ASSIGN to user_choice
  RETURN user_choice
END FUNCTION

``` 

``` plaintext 
START FUNCTION add_term(terms_dict)
  CALL INPUT("\tPlease enter the term-name: ") AND ASSIGN to term_name
  CALL INPUT("\tPlease enter the definition: ") AND ASSIGN to new_define
  IF term_name exists in terms_dict
    PRINT "\tTerm", term_name, "already exists. Consider updating the term instead."
  ELSE
    ADD new entry {term_name: [new_define]} to terms_dict
    PRINT "\tTerm", term_name, "added successfully."
  END IF
END FUNCTION
``` 

``` plaintext 
START FUNCTION update_term(terms_dict)
  CALL INPUT("\tPlease enter the term-name: ") AND ASSIGN to term_name
  IF term_name exists in terms_dict
    CALL INPUT("\tPlease enter the new definition: ") AND ASSIGN to new_define
    APPEND new_define to terms_dict[term_name]
    PRINT "\tDefinition updated for", term_name
  ELSE
    PRINT "\tTerm", term_name, "not found. Consider adding the term first."
  END IF
  END FUNCTION
``` 

``` plaintext 
START FUNCTION get_term(terms_dict)
  CALL INPUT("\tPlease enter the term-name: ") AND ASSIGN to term_name
  IF term_name exists in terms_dict
    PRINT "\n\t", term_name, ":", terms_dict[term_name]
  ELSE
    PRINT "\tTerm", term_name, "not found."
  END IF
END FUNCTION
``` 


<hr>

**Sample Application as Python Code**

```python
"""  
Sample App: Technology Terms Dictionary App
Description: A lookup app for technology terms and definitions.  
Author: Clinton Garwood  
Date: August 2024  
License: MIT  
"""
import os
import pickle


class Terms:
    def __init__(self, term_keyword, as_defined="unknown"):
        self.term_name = term_keyword
        self.definition = [as_defined]

    def set_term_name(self, term_name):
        self.term_name = term_name

    def set_definition(self, new_define):
        self.definition.append(new_define)

    def get_term_name(self):
        return self.term_name

    def get_definition(self):
        return self.definition


def terms_menu():
    print(f'\n\t1) Lookup a Term')
    print(f'\t2) Add a Term')
    print(f'\t3) Update a Term')
    print(f'\t4) Exit')
    return


def main():
    print(f'\nTechnical Term Lookup App')
    terms_dict = load_terms_dict('../../terms_dict.pkl')

    while True:
        terms_menu()
        user_choice = get_terms_choice()
        if user_choice == '1':
            get_term(terms_dict)
        elif user_choice == '2':
            add_term(terms_dict)
        elif user_choice == '3':
            update_term(terms_dict)
        elif user_choice == '4':
            save_terms_dict(terms_dict, '../../terms_dict.pkl')
            print(f'\tExiting... ')
            break
        else:
            print(f'\tInvalid choice. Please select again.')
    return


def load_terms_dict(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            terms_dict = pickle.load(f)
            print(f'\tLoaded terms from {filename}')
    else:
        terms_dict = {}
        print(f'\tNo existing data found. Starting fresh.')
    return terms_dict


def save_terms_dict(terms_dict, filename):
    with open(filename, 'wb') as f:
        pickle.dump(terms_dict, f)
        print(f'\tData saved to {filename}')


def get_terms_choice():
    user_choice = input("\tPlease select: ")
    return user_choice


def add_term(terms_dict):
    term_name = input("\tPlease enter the term-name: ").strip()
    new_define = input("\tPlease enter the definition: ").strip()
    if term_name in terms_dict:
        print(f'\tTerm "{term_name}" already exists. Consider updating the term instead.')
    else:
        terms_dict[term_name] = [new_define]
        print(f'\tTerm "{term_name}" added successfully.')
    return


def update_term(terms_dict):
    term_name = input("\tPlease enter the term-name: ").strip()
    if term_name in terms_dict:
        new_define = input("\tPlease enter another definition: ").strip()
        terms_dict[term_name].append(new_define)
        print(f'\tDefinition updated for "{term_name}".')
    else:
        print(f'\tTerm "{term_name}" not found. Consider adding the term first.')
    return


def get_term(terms_dict):
    term_name = input("\tPlease enter the term-name: ").strip()
    if term_name in terms_dict:
        print(f'\n\t{term_name}: {terms_dict[term_name]}')
    else:
        print(f'\tTerm "{term_name}" not found.')
    return


if __name__ == '__main__':
    main()


```

<hr>
