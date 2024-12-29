## App 2: Math Calculator
Simple menu-based calculator, which offers the user math options including:
- Addition
- Subtraction
- Multiplication 
- Division

App Type: Educational, Personal Improvement, Data Science<br>
Author: Clinton Garwood<br>
September 2024<br>
License: MIT<br>
<hr>

### Algorithm as Pseudocode

```text
START main function
    Print: "Welcome to the Math Calculator"
    Call user_prompt() and catch (menu_option, float_one, float_two)
    While menu_option is not 5:
        IF menu_option = 1:
            Call do_addition(float_one, float_two)
        IF menu_option = 2:
            Call do_subtraction(float_one, float_two)
        IF menu_option = 3:
            Call do_multiply(float_one, float_two)
        IF menu_option = 4:
            Call do_division(float_one, float_two)
        IF menu_option = 5:
            End While Loop
        IF menu_option = any other than 1, 2, 3, 4, 5:
            Print: "Invalid selection. Please try again."
        Re-call user_prompt and catch (menu_option, float_one, float_two)
    Print: "Thank you for using the Math Calculator App"
END
```

<br>

```text 
START user_prompt function
    Call the main_menu()
    Prompt the User for the Menu Option
    Prompt the User for the First Float
    Prompt the User for the Second Float
    Return menu_option, float_one, float_two
END
```

<br>

```text 
START main_menu function
    Print: 1) Do Addition
    Print: 2) Do Subtraction
    Print: 3) Do Multiplication
    Print: 4) Do Division
    Print: 5) Exit
END
```

<br>

```text
START do_addition function
    Takes two floats
      float_one: first number
      float_two: second number
      sum: (float_one + float_two)
      Print: "(float_one) + (float_two) = (sum)"
END
```

<br>

```text
START do_subtraction function
    Takes two floats
      float_one: first number
      float_two: second number
      difference: (float_one - float_two)
      Print: "(float_one) - (float_two) = (difference)"
END
```

<br>

```text
START do_multiply function
    Takes two floats
      float_one: first number
      float_two: second number
      product: (float_one * float_two)
      Print: "(float_one) x (float_two) = (product)"
END
```

<br>

```text
START do_division function
    Takes two floats
      float_one: first number
      float_two: second number
      Divide float_one by float_two
      quotient: (float_one / float_two)
        Handle the divide by zero errors properly
      Print: "(float_one) / (float_two) = (quotient)"
END
```