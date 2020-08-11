#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

# This script creates one name: first_fibs.
# It also prints the start of "Lateralus".

print('1 syllable(s):', 'Black')
print('1 syllable(s):', 'then')
print('2 syllable(s):', 'white are')
print('3 syllable(s):', 'all I see')
print('5 syllable(s):', 'in my infancy')
print('')

def first_fibs(N):
    """Returns a list of the first N Fibonacci numbers.
    
    Receives an int N bigger than or equal to 0, 
    and does what it says above.
    """

    f = []
    Danny, Carey = 0, 1

    for i in range(N):
        f.append(Carey)
        Danny, Carey = Carey, Danny + Carey

    return f

# If you are reading this text in Spyder, and 
# you press play, the following code will run.
if __name__ == '__main__':
    print('The first 5 Fibonacci numbers are:')
    print(first_fibs(5))

# If you are running this script as a consequence 
# of importing it, this code will not run.