## App 4: Quick Reference App

**Quick Reference for Technical Terms App**  
- **App Type:** Knowledge, Programming, Organization, Personal Improvement
- **Author:** Clinton Garwood  
- **November 2024** 
- **Description:** This application allows a user to add and/or lookup a summary of data for any keyword. The app uses the class `Terms`, and Python `pickle` for object storage. 
-  Class Representation: UML 
-  Algorithm Representation: Pseudocode
- 
**Design Document:**

**Class File `Terms` Representation as UML:**
### Class File: 

#### Unified Modeling Language (UML) Representation

``` plaintext

UML for Class File `Terms`
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
Python Class Name: `Terms` 

Attributes:
`term_name` is a label with private attribute (-) for type String.

`definition` is the full-text with private attribute (-) for type List[String].

Methods:
`__init__` constructor initializes the attributes. The default value as_defined is shown.

`set_term_name` and `set_definition` are public methods (+) and don't return values (void).

`get_term_name` and `get_definition` are public methods that return the corresponding attribute types (String and List[String]).


### Application Methods:
  <table>
  <tr><td>Add Term</td><td>add_term(terms_dict)</td></tr>
  <tr><td>Get Term</td><td> get_term(terns_dict)</td></tr>
  <tr><td>Get Choice</td><td>get_terms_choice()</td></tr>
  <tr><td>Load Terms</td><td>load_terms_dict(filename)</td></tr>
  <tr><td>The Main Program or App</td><td>main()</td></tr>
  <tr><td>Main Menu</td><td>terms_menu()</td></tr>
  <tr><td>Save Term</td><td>save_terms_dict(terms_dict, filename)</td></tr>
  <tr><td>Update Term</td><td>update_term(terns_dict)</td></tr>
</table>

**Algorithm Representation as Pseudocode:**

``` plaintext 
START CLASS Terms
  Attributes:
    term_name: string
    definition: list of strings
  
  Methods:
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

```

Main Menu: terms_menu()
``` plaintext 

START FUNCTION terms_menu
    PRINT "\n\t1) Lookup a Term"
    PRINT "\t2) Add a Term"
    PRINT "\t3) Update a Term"
    PRINT "\t4) Exit"
    RETURN
END FUNCTION

```

Main Program: main()
``` plaintext 
START FUNCTION main
  PRINT "\nTechnical Term Lookup App"
  CALL load_terms_dict('terms_dict.pkl') UPDATE terms_dict

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

Load Terms: load_terms_dict(filename)
``` plaintext 
## START FUNCTION load_terms_dict(filename)
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

Save Term: save_terms_dict(terms_dict, filename)
``` plaintext 
START FUNCTION save_terms_dict(terms_dict, filename)
  OPEN filename in 'wb' mode AND ASSIGN to f
  PICKLE dump terms_dict into f
  PRINT "\tData saved to", filename
END FUNCTION
```

Get Choice: get_terms_choice()
``` plaintext 
START FUNCTION get_terms_choice
  CALL INPUT("\tPlease select: ") AND ASSIGN to user_choice
  RETURN user_choice
END FUNCTION
```

Add Term: add_term(terms_dict)
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

Update Term: update_term(terns_dict) 
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

Get Term: get_term(terns_dict) 
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

