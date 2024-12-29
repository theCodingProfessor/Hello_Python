### Lab 13: Multi-Dimensional Arrays

#### Assignment Overview
In this lab, you will work with multidimensional arrays using tuples and lists. You will learn to represent tabular data with both row and column-based tuples, convert them into matrices (lists of lists), and print these matrices using various methods including indexing, loops, and list transposition.

#### Learning Objectives
- Understand the use of tuples and lists for representing multidimensional data.
- Learn to convert tuples into lists of lists (matrices).
- Practice printing tabular data using different techniques, including nested indexing, loops, and list transposition.

- The three-by-three rows/column table we will consider is as follows. Rows are (left-to-right) and columns are (top-to-bottom).

|           | c1 | c2 | c3  |
|:---------:|:---:|:---:|:---:|
|  **r1**   | X | R | S |
|  **r2**   | L | Y | T |
|  **r3**   | M | N | Z |

#### Instructions
Explore representations of data, as a Table, using python `list()`

**13.1) Create File**  
- Create a properly formatted Python file named `matrix_table.py`.

**13.2) Define `main()` Function**  
Define a function named `main`. Inside this function, create a welcome statement that announces the intention of the lab and initialize the following tuples:
```python
def main():
    print(f'\nWelcome to Lab 13: Multi-Dimensional Arrays.')

    r1 = ('X', 'R', 'S')
    r2 = ('L', 'Y', 'T')
    r3 = ('M', 'N', 'Z')
    c1 = ('X', 'L', 'M')
    c2 = ('R', 'Y', 'N')
    c3 = ('S', 'T', 'Z')

    # Your code will go here

    return
```

**3.3) Row Data**

**Print Table Using Row Tuples**: Print out a table representation using the row tuples with single indexing.
```python
    print(f'\nPrinting Table: Using Row Tuples')
    print(f'\t{r1[0]} | {r1[1]} | {r1[2]}')
    print(f'\t{r2[0]} | {r2[1]} | {r2[2]}')
    print(f'\t{r3[0]} | {r3[1]} | {r3[2]}')
```

**Create and Print Row Matrix**: Combine the row tuples into a matrix named `row_matrix` and print its values.
```python
    row_matrix = [r1, r2, r3]
    print(f'\nRaw values of row_matrix: {row_matrix}')
```

**Print Table Using Nested Indexing**: Use `row_matrix` and nested indexing to print the table without a loop.
```python
    print(f'\nPrinting Table: Using nested indexing row_matrix[index][index]')
    print(f'\t{row_matrix[0][0]} | {row_matrix[0][1]} | {row_matrix[0][2]}')
    print(f'\t{row_matrix[1][0]} | {row_matrix[1][1]} | {row_matrix[1][2]}')
    print(f'\t{row_matrix[2][0]} | {row_matrix[2][1]} | {row_matrix[2][2]}')
```

**Print Table Using Loop**: Use a loop with `row_matrix` to print the table.
```python
    print(f'\nTable Representation: row_matrix and a loop')
    for each in row_matrix:
        print(f'\t{each[0]} | {each[1]} | {each[2]}')
```

**13.4) Column Data**

**Print Table Using Column Tuples**: Print out a table representation using the column tuples with single indexing.
```python
    print(f'\nPrinting Table: Using Column Tuples')
    print(f'\t{c1[0]} | {c2[0]} | {c3[0]}')
    print(f'\t{c1[1]} | {c2[1]} | {c3[1]}')
    print(f'\t{c1[2]} | {c2[2]} | {c3[2]}')
```

**Create and Print Column Matrix**: Combine the column tuples into a matrix named `col_matrix` and print its values.
```python
    col_matrix = [each for each in (c1, c2, c3)]
    print(f'\nRaw Values of col_matrix: {col_matrix}')
```

**Print Table Using Nested Indexing**: Use `col_matrix` and nested indexing to print the table without a loop.
```python
    print(f'\nPrinting Table: Using nested indexing col_matrix[index][index]')
    print(f'\t{col_matrix[0][0]} | {col_matrix[1][0]} | {col_matrix[2][0]}')
    print(f'\t{col_matrix[0][1]} | {col_matrix[1][1]} | {col_matrix[2][1]}')
    print(f'\t{col_matrix[0][2]} | {col_matrix[1][2]} | {col_matrix[2][2]}')
```

**Print Table Using Loop**: Use a loop with `col_matrix` to print the table.
```python
    print(f'\nTable Representation: col_matrix and loop')
    for each in range(len(col_matrix[0])):  # Iterate over the number of elements in a column (rows)
        print(f'\t{col_matrix[0][each]} | {col_matrix[1][each]} | {col_matrix[2][each]}')
```

**Print Table Using Transposition**: Use the `zip(*)` feature to transpose `col_matrix` and print the table.
```python
    print(f'\nTable Representation: col_matrix, loop and zip(*)')
    for each, value in enumerate(list(zip(*col_matrix))):
        print(f'\t{value[0]} | {value[1]} | {value[2]}')
```

#### Submission
Submit a single source code file named: `matrix_table.py`.

#### Assessment Criteria
- Correct definition and initialization of tuples and matrices.
- Accurate printing of the table using row and column tuples.
- Proper conversion of tuples to matrices and accurate printing using nested indexing and loops.
- Correct usage of the `zip(*)` function for matrix transposition and printing.

#### Additional Notes
- Ensure your script is properly configured with headers.
- Test your code thoroughly to verify correct table representation.
- Use comments to explain each section of your code for clarity.

<hr>

#### Additional Code
Demonstration File 

```python
"""
Module Name: Programming Lab 13
Description: Matrix as Multi-Dimensional Arrays
Author: Clinton Garwood
Date: August 2024
License: MIT
"""


def main():
    print(f'\nWelcome to Lab 13: Matrix as Multi-Dimensional Arrays.')

    # Row Tuples
    r1 = ('X', 'R', 'S')
    r2 = ('L', 'Y', 'T')
    r3 = ('M', 'N', 'Z')

    # Using only the row tuples print out an accurate representation of the table.
    print(f'\nPrinting Table: Using Row Tuples')
    print(f'\t{r1[0]} | {r1[1]} | {r1[2]}')
    print(f'\t{r2[0]} | {r2[1]} | {r2[2]}')
    print(f'\t{r3[0]} | {r3[1]} | {r3[2]}')

    # Combine the row tuples into a matrix (list of lists)
    row_matrix = [r1, r2, r3]
    print(f'\nRaw values of row_matrix: {row_matrix}')

    # Use the row_matrix[index][index] syntax to print the table
    print(f'\nPrinting Table: Using nested indexing row_matrix[index][index]')
    print(f'\t{row_matrix[0][0]} | {row_matrix[0][1]} | {row_matrix[0][2]}')
    print(f'\t{row_matrix[1][0]} | {row_matrix[1][1]} | {row_matrix[1][2]}')
    print(f'\t{row_matrix[2][0]} | {row_matrix[2][1]} | {row_matrix[2][2]}')

    # Use a loop and the row_matrix to print an accurate representation of the table
    print(f'\nTable Representation: row_matrix and a loop')
    for each, value in enumerate(row_matrix):
        print(f'\t{value[0]} | {value[1]} | {value[2]}')

    # Columns Tuples Section
    c1 = ('X', 'L', 'M')
    c2 = ('R', 'Y', 'N')
    c3 = ('S', 'T', 'Z')

    # Using only the column tuples print out an accurate representation of the table.
    print(f'\nPrinting Table: Using Column Tuples')
    print(f'\t{c1[0]} | {c2[0]} | {c3[0]}')
    print(f'\t{c1[1]} | {c2[1]} | {c3[1]}')
    print(f'\t{c1[2]} | {c2[2]} | {c3[2]}')

    # Use list comprehension to combine the column tuples into a matrix (list of lists)
    col_matrix = [each for each in (c1, c2, c3)]
    print(f'\nRaw Values of col_matrix: {col_matrix}')

    # Use the col_matrix[index][index] syntax to print the table
    print(f'\nPrinting Table: Using nested indexing col_matrix[index][index]')
    print(f'\t{col_matrix[0][0]} | {col_matrix[1][0]} | {col_matrix[2][0]}')
    print(f'\t{col_matrix[0][1]} | {col_matrix[1][1]} | {col_matrix[2][1]}')
    print(f'\t{col_matrix[0][2]} | {col_matrix[1][2]} | {col_matrix[2][2]}')

    # Use a loop and the col_matrix to print an accurate representation of the table
    print(f'\nTable Representation: col_matrix and loop')
    for each in range(len(col_matrix[0])):  # Iterate over the number of elements in a column (rows)
        print(f'\t{col_matrix[0][each]} | {col_matrix[1][each]} | {col_matrix[2][each]}')

    # Transposing: Alternate loop for col_matrix using zip(*)
    # Turning rows > columns or columns > rows is called Transposing
    # To transpose col_matrix into row_matrix we can use:
    # We can however transpose the matrix using zip(*col_matrix)
    new_row_matrix = list(zip(*col_matrix))

    # This feature can streamline our loop of columns as follows:
    print(f'\nTable Representation: col_matrix, loop and zip(*)')
    for each, value in enumerate(list(zip(*col_matrix))):
        print(f'\t{value[0]} | {value[1]} | {value[2]}')

    return


main()

```

<hr>
