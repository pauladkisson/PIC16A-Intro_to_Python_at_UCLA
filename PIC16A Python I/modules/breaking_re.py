#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""




# Running the code below with the 
# two commented-out lines works fine.
# It makes use of the 
# re (regular expressions) library.

# I found the source code for re.
# On my machine it's located at 
# /opt/miniconda3/lib/python3.7/re.py

# I found that almost all the 
# functions in this script 
# make use of a hidden function _compile.
# This function calls sre_compile.compile 
# in most scenarios.

# The commented lines import sre_compile 
# and change the definition of 
# sre_compile.compile to nonsense.

# Uncomment the two lines of code, 
# restart the console, and run the script again.
# You'll get a hideous error message.
# Yes, Python lets us destroy modules!!




# import sre_compile
# sre_compile.compile = lambda x:0

import re

regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, "June 24")

print("Month: %s" % (match.group(1)))
print("Day: %s" % (match.group(2)))