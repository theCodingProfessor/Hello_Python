### Lab 12: Arrays as Lists (Mutable) and Tuples (Immutable)

#### Assignment Overview
In this lab, you will learn to work with Python lists and tuples, convert integer values to various string representations, and perform data type conversions. You will use different methods to populate Python lists and extract even values using appropriate conversion methods.

#### Learning Objectives
- Understand the difference between lists (mutable) and tuples (immutable) in Python.
- Learn to use `while` loops, `for` loops, and list comprehension to manipulate data.
- Gain experience with Python's built-in functions for data type conversions: `bin()`, `oct()`, `hex()`, and `int()`.

#### Instructions
Explore data collections including lists and tuples

**12.1) Create File**  
- Create a properly formatted Python file named `array_lists.py`.

**12.2) Define `main()` Function**  
Define a function named `main`. Inside this function, create a welcome statement that announces the intention of the lab and also a tuple named `integer_tuple` containing integer values from 0 to 10.
```python
def main():
    print(f'\nWelcome to Lab 12: Arrays as Lists and Tuples.')

    integer_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    return
```

**12.3) Populate Lists**  
You will populate Python lists with different methods including `while` loop, `for` loop, and list comprehension. Use Python's built-in functions `bin()`, `oct()`, and `hex()` for these conversions.

**Binary Conversion**: Use a `while` loop to convert and store the binary representation of each integer in `integer_tuple` to `binary_list`.
```python
    binary_list = list()
    while_count = 0
    while while_count < 11:
        binary_list.append(bin(integer_tuple[while_count]))
        while_count += 1
```

**Octal Conversion**: Use a `for` loop to convert and store the octal representation of each integer in `integer_tuple` to `octal_list`.
```python
    octal_list = list()
    for each, value in enumerate(integer_tuple):
        octal_list.insert(each, oct(value))
```

**Hexadecimal Conversion**: Use list comprehension to convert and store the hexadecimal representation of each integer in `integer_tuple` to `hex_list`.
```python
    hex_list = [hex(each) for each in integer_tuple]
```

**Print Lists**: Print each of these populated lists with a corresponding label.
```python
    print(f'Binary list: {binary_list}')
    print(f'Octal list: {octal_list}')
    print(f'Hexadecimal list: {hex_list}')
```

**12.4) Extract and Print Even Values**  
Use the indexing feature of lists to unpack even values (0, 2, 4, ...) using `while` loops, `for` loops, and list comprehension. Use the built-in `int()` conversion function with the appropriate base.

**From `binary_list`**: Use a `while` loop and `int(binary_string, 2)` to print even values.
```python
    list_count = 0
    print(f'\nEven values (as integers) from binary list')
    while list_count < 11:
        print(f'\t{int(binary_list[list_count], 2)}')
        list_count += 2
```

**From `octal_list`**: Use a `for` loop and `int(octal_string, 8)` to print even values.
```python
    print(f'\nEven values (as integers) from octal list')
    for each in range(0, len(octal_list), 2):
        print(f'\t{int(octal_list[each], 8)}')
```

**From `hex_list`**: Use list comprehension and `int(hex_string, 16)` to print even values.
```python
    print(f'\nEven values (as integers) from hex list {[int(hex_list[i], 16) for i in range(0, len(hex_list), 2)]}')
```

#### Submission
Submit a single source code file named: `array_lists.py`.

#### Assessment Criteria
- Correctly defined `main()` function with appropriate welcome statement and tuple initialization.
- Proper use of `while` loop, `for` loop, and list comprehension to populate lists.
- Accurate conversion of integer values to binary, octal, and hexadecimal string representations.
- Correct extraction and printing of even values from each list using appropriate conversion methods.

#### Additional Notes
- Ensure your script is properly configured with headers.
- Test your code thoroughly to ensure all conversions and extractions are accurate.
- Use comments to explain the purpose of each section of your code.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 12
Description: Arrays as Lists and Tuples
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def main():
    print(f'\nWelcome to Lab 12: Arrays as Lists and Tuples.')

    integer_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    binary_list, octal_list, hexadecimal_list = list(), list(), list()
    while_count = 0
    while while_count < 11:
        binary_list.append(bin(integer_tuple[while_count]))
        while_count += 1

    for each, value in enumerate(integer_tuple):
        octal_list.insert(each, oct(value))

    hexadecimal_list = [hex(each) for each in integer_tuple]

    print(f'\nLists of lists')
    print(f'\tbin list {binary_list}')
    print(f'\toct list {octal_list}')
    print(f'\thex list {hexadecimal_list}')

    list_count = 0
    print(f'\nEven values (as integers) printed from binary list')
    while list_count < 11:
        print(f'\t{int(binary_list[list_count], 2)}')
        list_count += 2

    print(f'\nEven values (as integers) printed from octal list')
    for each in range(0, 12, 2):
        print(f'\t{int(octal_list[each], 8)}')

    print(f'\nEven values (as integers) from hex list {[int(hexadecimal_list[i], 16) for i in range(0, len(hexadecimal_list), 2)]}')

    return


main()

```

<hr>
