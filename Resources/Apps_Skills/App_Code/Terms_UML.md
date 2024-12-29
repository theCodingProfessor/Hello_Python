
## Code and Terms Lookup: App #4

### Class File: `Terms` 

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

### Categories Described

Class Name:

`Terms` 

Attributes:

`term_name` is a label with private attribute (-) for type String.

`definition` is the full-text with private attribute (-) for type List[String].

Methods:

`__init__` constructor initializes the attributes. Default value for as_defined is shown.

`set_term_name` and `set_definition` are public methods (+) and don't return values (void).

`get_term_name` and `get_definition` are public methods that return the corresponding attribute types (String and List[String]).

