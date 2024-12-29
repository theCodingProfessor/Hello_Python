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

    # Using only the row tuples, print out an accurate representation of the table.
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

    # Using only the column tuples, print out an accurate representation of the table.
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
