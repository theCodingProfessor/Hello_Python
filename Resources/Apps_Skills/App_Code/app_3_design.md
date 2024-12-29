## App 3: Personal Journal

**A Personal Journal (Text-File Storage) App**  
- **App Type:** Productivity, Self Improvement
- **Author:** Clinton Garwood  
- **August 2024** 
- **Description:** This application allows a user to make new journal entries, look at the most recent journal entries, or read the entire text file
-  Algorithm Representation: Pseudocode
	
---

**Design Document Pseudocode**

List of Functions/Features:
- main
- configure_file(string_file_name)
- journal_menu()
- get_journal_choice()
- add_entry(string_file_name)
- most_recent(string_file_name, integer_lines)
- read_all(string_file_name)


``` plaintext 
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
```

``` plaintext 
START FUNCTION journal_menu
    PRINT "1) Add Entry"
    PRINT "2) Read Most Recent Entry"
    PRINT "3) Read All Entries"
    PRINT "4) Exit"
END FUNCTION
```

``` plaintext 
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

START FUNCTION get_journal_choice
    PROMPT user TO INPUT a choice
    RETURN user_choice
END FUNCTION
```

``` plaintext 
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
```

``` plaintext 
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
```

``` plaintext 
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
