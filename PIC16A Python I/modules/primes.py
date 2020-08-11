#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

# This script creates two names:
# first_primes and Grothendieck

def first_primes(N):
    """Returns a list of the first N prime numbers.
    
    Receives an int N bigger than or equal to 0, 
    and does what it says above.
    """

    ps = []
    potentialPrime = 2

    while len(ps) < N:
        for p in ps:
            if potentialPrime % p == 0:
                break
        else:
            ps.append(potentialPrime)

        potentialPrime += 1
    return ps

# https://en.wikipedia.org/wiki/57_(number)
Grothendieck = 57

# If you are reading this text in Spyder, and 
# you press play, the following code will run.
if __name__ == '__main__':
    print('The first 20 primes are:')
    print(first_primes(20))

# If you are running this script as a consequence 
# of importing it, this code will not run.