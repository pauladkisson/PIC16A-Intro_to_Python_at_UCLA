#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

#%%
# Run this cell-by-bell using the button two to the right of 'play'.

#%%
import fib

#%%
import fib                     # The script is only ran once.

#%%
print(first_fibs(5))           # We have to access the module's namespace...

#%%
print(fib.first_fibs(5))       # ...like this.
print('')

#%%
import primes
print(primes.first_primes(20)) # Similarly...
print(primes.Grothendieck)     # we can access non-functions;
print('')                      # unsurprising, given how Python works.

#%%
# It is customary to place import statements
# at the top but it is not required.
# I often violate this custom.
# I should probably be a better person.

#%%
# There's a Python module called 'math'.
# Unsurprising it has a variable called pi.
# We could import math, and then use math.pi,
# or...

from math import pi
print(pi)

#%%
# Also, suppose we want all the math
# but we are too lazy to type all four
# letters of the word 'math' every time.
# Then we could do this...

import math as m
print(m.acos(-1))              # arc cosine of -1 is also pi.

#%%
# Suppose we want pi but we are too lazy to
# type all two letters every time we want pi.
# Then we could do this...

from math import pi as p
print(p)
print('')

#%%
# What if you print a module name?
print(fib)
print(primes)
print(m)
print('')
# It tells us where the module is stored on your computer!

#%%
# How does your computer find modules?
# It looks in the directory of the current script,
# as well as in some locations that Anaconda will
# have organized for you correctly (hopefully).
import sys
print(sys.path)
print('')

# On my computer...
# lib/python3.7               I can see threading, timeit, re, random.
#                             this.py is quite a funny file.
# lib/python3.7/lib-dynload   Here, I can see math.
# lib/python3.7/site-packages Here, I can see numpy, matplotlib, scikit_learn.

#%%
# If you want to know every variable/function in a module you can use dir.
for module in [fib, primes, m]:
    print(module.__name__, 'has')
    print(dir(module))
    print('')

#%%
# Now we can finally see what Python makes available to us from the start.
import builtins
print(dir(builtins))
print('')
# So many ways to make an error!

#%%
print(sys.argv)
# To see the benefit of this line
# change to tutorial_0c.py and read the instructions there.