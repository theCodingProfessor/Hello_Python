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
