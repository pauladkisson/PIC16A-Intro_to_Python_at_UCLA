#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""


#%% HOW IMPORT STATEMENTS WORK
# Suppose we're in the middle of script.py
# and we encounter the statement "import mod"
# where mod.py is another script. What happens?

# 1) If "mod" has not already appeared in an import statement,
#    then the code in mod.py is executed with __name__ == 'mod'.
# 2) After 1), a lookup procedure (namespace) is created so that
#    "mod.name" in script.py refers to the same object
#    as "name" in mod.py.

# The script that triggers Python to run is
# executed with __name__ == '__main__'.


#%% DEMO
# This code demonstrates two things.

# First, it shows what happens when a module is imported for the second time.
#   "import import_2b" causes the code in import_2b.py to execute.
#   One of the lines in import_2b.py says "import import_2a".
#   Since we have already encountered a line that reads "import import_2a",
#   the code in import_2a.py is NOT executed for a second time.
#   However, a lookup procedure is still created, so that
#   "import_2a.var" in import_2b.py refers to "var" in import_2a.py.

# Second, it shows how the lookup procedures work.
#   Three look up procedures are created.
#    - First, "import import_2a" in this file creates a lookup procedure.
#    - Second, "import import_2a" in "import_2b.py" creates a lookup procedure.
#    - Third, "import import_2b" in this file creates a lookup procedure.
#
#   This provides us with two ways to access the variables in import_2a.py:
#    - directly using import_2a.var;
#    - via import_2b.py using import_2b.import_2a.var.
#   We write code to highlight that these names are accessing the same object.

print('Before "import import_2a"')
print('')

import import_2a

print('')
print('After "import import_2a"')

print('Before "import import_2b"')
print('')

import import_2b

print('')
print('After "import import_2b"')

if import_2a.var is import_2b.import_2a.var:
    print('import_2a.var is import_2b.import_2a.var')

print('         ', import_2a.var, '||', import_2b.import_2a.var)

import_2a.var = [1]
print('         ', import_2a.var, '||', import_2b.import_2a.var)

import_2b.import_2a.var = [2]
print('         ', import_2a.var, '||', import_2b.import_2a.var)