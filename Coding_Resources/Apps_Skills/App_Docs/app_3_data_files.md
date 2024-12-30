### Application 3: Data Structures and Files
**Topics:** Data Structures, File Read and Write

<hr>

### 1. Objective
**Purpose:**  
- This assignment asks you to design and implement a Python application that interacts with a file to read and write data. 
- You will incorporate file I/O (read and write) operations as a distinct module within your application. 
- Connect user interaction with data representations and storage such as managing a list of items.
- Demonstrate Python functions with data structure support file handling.
- Consider an app idea of your own, different from the example provided. 

**Pathway:**
1) Describe a simple application using pseudocode or another type of design document instrument.
2) Convey the logic of the application (algorithm) proposed into its template.
3) The formatted design document containing the algorithm is the `specification` which guide the creation of the Python application.
4) Build the Python app from the `specification`

#### Data Storage Concepts:
Experimenting in a topic area of interest to you is encouraged (but not required).
Select a concept and define its design (algorithm) document before creating code.
-- Create and read logfiles (networking, programming)
-- Create and manage a User Access List (IT, cybersecurity)
-- Back up a file/directory (IT, data engineering)
-- Personal Journal (programming, services)

<hr>

### 2. Learning Outcomes

- **Design:** Create a pseudocode or design document that outlines the core logic of an application, including file I/O operations and Python functions.
- **Develop:** Translate your design document into a fully functional Python program that reads and writes data to a file.
- **Troubleshoot:** Debug and resolve logical errors in your program, documenting them in a Change Log.

<hr>

### 3. Assignment Instructions

**Part 1-1: Initialize a Design Document**  
- **Working Title:** Provide a meaningful title for your app.
- **Author Information:** Include your name.
- **Description:** Write a short description of the algorithm or app.
- **Representation(s):** Use pseudocode.

**Part 1-2: Define the Algorithm as Pseudocode
- Declare a program START 
- For each Function in the Application:
	- Declare a START_FUNCTION_NAME
		- Define each step (first, next... last... etc., as needed)
	- Declare an END_FUNCTION_NAME
- When all the functions have been START_FUNCTION::STOP_FUNCTION defined, declare a program STOP 

**Part 2: Create the Application**  
- **Translation:** Convert the design document into a working Python app.
- **Change Log:** If you encounter logic errors during coding (e.g., steps out of order, missing loops), make the necessary corrections in the code. Document these changes in a multi-line comment section titled **"Change Log"** at the top of your code.

<hr>

### 4. Submission Requirements

- **Design Document:** Submit a design document. Markdown (.md), PDF (.pdf) or MS Word (.docx) document types.
- **Python Code:** Submit a Python file (.py). Add a change log section (if applicable).

<hr>

### 5. Success Criteria
- **Design Document:**  
  - The required header is present
  - Visual indentation of functions and code logic in pseudocode.
  - Visual separation of each function in the pseudocode document

- **Python Code:**  
  - Correct implementation of the design.
  - Functionality and correctness of the code.
  - Handle errors and logic issues.

- **Change Log:**  
  - Accurate and clear documentation of any issues encountered and the changes made.

<hr>

### 6. Samples

**A Personal Journal (Text-File Storage) App**  
- **App Type:** Productivity, Self Improvement
- **Author:** Clinton Garwood  
- **August 2024** 
- **Description:** This application allows a user to make new journal entries, look at the most recent journal entries, or read the entire text file
-  Algorithm Representation: Pseudocode
	
<hr>

**Design Document Pseudocode Example**

```markdown
# Pseudocode: Personal Journal App
### Description:
This app adds text (with a timestamp) to a file. It offers menu options for adding, reading, and accessing journal entries.

<hr>

START MAIN
    PRINT "Welcome to the Personal Journal App."
    SET result TO 0
    SET journal_file_name TO 'the_journal.txt'
    CALL configure_file(journal_file_name)

    WHILE True
        CALL journal_menu()
        SET user_choice TO CALL get_journal_choice()

        IF user_choice IS '1'
            CALL add_entry(journal_file_name)
        ELSE IF user_choice IS '2'
            CALL most_recent(journal_file_name, 5)
        ELSE IF user_choice IS '3'
            CALL read_all(journal_file_name)
        ELSE IF user_choice IS '4'
            PRINT "Exiting..."
            BREAK
        ELSE
            PRINT "Invalid choice. Please select again."
    END WHILE

    PRINT "A Journal Links Your Goals to your Data."
END MAIN

<hr>

START FUNCTION journal_menu
    PRINT "1) Add Entry"
    PRINT "2) Read Most Recent Entry"
    PRINT "3) Read All Entries"
    PRINT "4) Exit"
END FUNCTION

<hr>

START FUNCTION configure_file(journal_file_name)
    IF journal_file_name DOES NOT EXIST
        OPEN journal_file_name FOR WRITING
        WRITE "This file journal_file_name created" + current timestamp TO file
        PRINT "New file created and written to."
    ELSE
        OPEN journal_file_name FOR APPENDING
        WRITE "Journal Menu Access" + current timestamp TO file
        PRINT "Journal Access Confirmed."
    END IF
END FUNCTION

<hr>

START FUNCTION get_journal_choice
    PROMPT user TO INPUT a choice
    RETURN user_choice
END FUNCTION

<hr>

START FUNCTION add_entry(journal_file_name)
    PROMPT user TO INPUT new journal entry INTO new_entry
    IF journal_file_name DOES NOT EXIST
        OPEN journal_file_name FOR WRITING
        WRITE "This file journal_file_name created" + current timestamp TO file
        WRITE new_entry + current timestamp TO file
        PRINT "New file created and written to."
    ELSE
        OPEN journal_file_name FOR APPENDING
        WRITE new_entry + current timestamp TO file
        PRINT "Journal Update Confirmed."
    END IF
END FUNCTION

<hr>

START FUNCTION most_recent(journal_file_name, n_lines)
    IF journal_file_name EXISTS
        OPEN journal_file_name FOR READING
        READ all lines INTO full_text
        SET recent_lines TO last n_lines OF full_text
        PRINT "Last n_lines entries of the journal:"

        FOR EACH line IN recent_lines
            PRINT line WITHOUT extra newlines

        OPEN journal_file_name FOR APPENDING
        WRITE "Read Access Part:" + current timestamp TO journal_file_name
    END IF
END FUNCTION

<hr>

START FUNCTION read_all(journal_file_name)
    IF journal_file_name EXISTS
        OPEN journal_file_name FOR READING
        READ all lines INTO full_text
        PRINT "Full Journal:"

        FOR EACH line IN full_text
            PRINT line WITHOUT extra newlines

        OPEN journal_file_name FOR APPENDING
        WRITE "Read Access Full:" + current timestamp TO journal_file_name
    END IF
END FUNCTION

```

<hr>

**Sample Application as Python Code**

```python

"""  
Sample App: The Personal Journal App  
Description: This app adds text (with a timestamp) to a file.  
Author: Clinton Garwood  
Date: August 2024  
License: MIT """
import os
import datetime


def journal_menu():
    print(f'\n\t1) Add Entry')
    print(f'\t2) Read Most Recent Entry')
    print(f'\t3) Read All Entries')
    print(f'\t4) Exit')
    return


def main():
    print(f'Welcome to the Personal Journal App.')
    result = 0
    journal_file_name = '../../the_journal.txt'
    configure_file(journal_file_name)
    while True:
        journal_menu()
        user_choice = get_journal_choice()
        if user_choice == '1':
            add_entry(journal_file_name)
        elif user_choice == '2':
            most_recent(journal_file_name, 5)
        elif user_choice == '3':
            read_all(journal_file_name)
        elif user_choice == '4':
            print(f'\tExiting... ')
            break
        else:
            print(f'\tInvalid choice. Please select again.')
    print(f'\nA Journal Links Your Goals to your Data.')
    return


def configure_file(journal_file_name):
    # Create a new file in the directory  
    if not os.path.exists(journal_file_name):
        with open(journal_file_name, 'w') as f:
            f.write(f'This file {journal_file_name} created {datetime.datetime.now()}\n')
            print(f'\t\tNew file created and written to.')
    else:
        with open(journal_file_name, 'a') as f:
            f.write(f'Journal Menu Access {datetime.datetime.now()}\n')
            print(f'\t\tJournal Access Confirmed.')

        return


def get_journal_choice():
    user_choice = input("\tPlease select: ")
    return user_choice


def add_entry(journal_file_name):
    # Collect Journal Entry Data  
    new_entry = input("Journal Entry... : ")
    if not os.path.exists(journal_file_name):
        with open(journal_file_name, 'w') as f:
            f.write(f'This file {journal_file_name} created {datetime.datetime.now()}\n')
            f.write(f'{new_entry}, {datetime.datetime.now()}\n')
            print(f'\t\tNew file created and written to.')
    else:
        with open(journal_file_name, 'a') as f:
            f.write(f'{new_entry}, {datetime.datetime.now()}\n')
            print(f'\t\tJournal Update Confirmed.')
    return


def most_recent(journal_file_name, n_lines):
    if os.path.exists(journal_file_name):
        with open(journal_file_name, 'r') as journal:
            # Read all the lines from the file  
            full_text = journal.readlines()

            # Ensure you don't try to read more lines than exist  
            recent_lines = full_text[-n_lines:]  # Get the last 'n' lines  

            print(f'\t\tLast {n_lines} entries of the journal:')
            for line in recent_lines:
                print(f'\t\t{line.strip()}')  # Print without a newline  

        # Log access time in append mode
        with open(journal_file_name, 'a') as journal:
            journal.write(f'Read Access Part: {datetime.datetime.now()}\n')
    return


def read_all(journal_file_name):
    if os.path.exists(journal_file_name):
        with open(journal_file_name, 'r') as journal:
            # Read all the lines from the file  
            full_text = journal.readlines()

            # Get all the lines  
            all_lines = full_text[:]

            print(f'\t\tFull Journal::')
            for line in all_lines:
                print(f'\t\t{line.strip()}')  # Print without a newline  

                # Log access time in append mode
                with open(journal_file_name, 'a') as journal_write:
                    journal_write.write(f'Read Access Full: {datetime.datetime.now()}\n')
    return


main()

```

<hr>
