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
# This code demonstrates three things:
# 1) "import import_1" executes the code in import_1.py;
# 2) after the import statement import_1.L and import_1.f
#    can be used to access L and f in import_1.py;
# 3) how the variable __name__ works.

import import_1    # code from import_1.py is executed
print('')          # with __name__ == 'import_1'

print(import_1.L)  # accesses the L defined in import_1.py
import_1.f()       # accesses the f defined in import_1.py

print(import_1.L)
print('')

import_1.L = ['Created in tutorial_1.py']
print(import_1.L)

import_1.f()
print(import_1.L)
print('')

print('__name__ ==', __name__)