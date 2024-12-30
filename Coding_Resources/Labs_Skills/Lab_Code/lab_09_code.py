"""
Module Name: Programming Lab 9
Description: Outer and Inner Loops (Nested Loops)
Author: Clinton Garwood
Date: August 2024
License: MIT
"""

print(f'\nWelcome to Lab 9: Outer and Inner Loops (Nested Loops)')

# Initialize Data
stop_up, stop_down = 4, 0
print(f'\nThe stop_up variable is {stop_up} of type {type(stop_up)}')
print(f'The stop_down variable is {stop_down} of type {type(stop_down)}')

# Count Up Outer and Inner Loops
print(f'\nIncrementing Nested Loops')
for out_loop_1 in range(1, stop_up):
    for in_loop_1 in range(1, stop_up):
        print(f'\tOuter Counter {out_loop_1} Inner Loop {in_loop_1}')
    print()

# Count Down Outer and Inner Loops
print(f'\nDecrementing Nested Loops')
for out_loop_2 in range(3, stop_down, -1):
    for in_loop_2 in range(3, stop_down, -1):
        print(f'\tOuter Counter {out_loop_2} Inner Loop {in_loop_2}')
    print()
