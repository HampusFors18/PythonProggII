"""
Solutions to exam tasks for modul 1
Name: Hampus Naumanen
Code: AX-0055-ZCW
"""

import random
import time
import math


        

def count_sublists(lst):
    """ A1: Return the number of sublists in lst """
    count = 0
    if not isinstance(lst, list):
        return 0
    else:
        for x in lst:
            if isinstance(x, list):
                count += 1 + count_sublists(x)
    return count


def c(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        return c(n-1) + c(n-2) + c(n-3)

#This method also works and is very easy to use in python
# import functools
# @functools.lru_cache(None)
# def c_mem(n):
    
#     """ A2:
#         Compute c(n) recursively as above but use 
#         memorization to keep the runtime down.
#     """
#     if n < 2:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return c_mem(n-1) + c_mem(n-2) + c_mem(n-3)
    

def c_mem(n, memory = {0:0, 1:0, 2:1}):
    """ A2:
#         Compute c(n) recursively as above but use 
#         memorization to keep the runtime down.
#     """
    if n in memory:
        return memory[n]
    else:
        memory[n] = c_mem(n-1, memory) + c_mem(n-2, memory) + c_mem(n-3, memory)
        return memory[n]


def main():
    print('Test of count_sublists')
    print(count_sublists(1), '  Expected result: 0 (argument is not a list)')
    print(count_sublists([]), '  Expected result: 0 (no sublists in argument)')
    print(count_sublists([1, 2]),
          '  Expected result: 0 (no sublists in argument)')
    print(count_sublists([[], 1, 2]), '  Expected result: 1')
    print(count_sublists([[1], 2, [3]]), '  Expected result: 2')
    print(count_sublists([[1, [2]], [1], 2]), '  Expected result: 3')
    print(count_sublists([[[[]]]]), '  Expected result: 3')
    

    print('\nTest of c_mem')
    print('c_mem( 1)', c_mem(1), ' Expected 0')
    print('c_mem( 2)', c_mem(2), ' Expected 1')
    print('c_mem( 3)', c_mem(3), ' Expected 1')
    print('c_mem( 4)', c_mem(4), ' Expected 2')
    print('c_mem( 5)', c_mem(5), ' Expected 4')
    print('c_mem(10)', c_mem(10), ' Expected 81')
    print('c_mem(11)', c_mem(11), ' Expected 149')
    print('c_mem(12)', c_mem(12), ' Expected 274')
    print('c_mem(13)', c_mem(13), ' Expected 504')
    print('c_mem(100):', c_mem(100), ' Expected ?')

    print('\nCode for task B1')


if __name__ == "__main__":
    main()
    print('Over and out')

print("""
Answer to task B1:




""")
