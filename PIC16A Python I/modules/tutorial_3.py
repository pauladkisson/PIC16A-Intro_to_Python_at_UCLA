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
# This code emphasizes that the lookup procedure can apply to
# variables that didn't exist when the lookup procedure was created.

import import_3
print('')

import_3.print_i()

try:
    import_3.print_j()
except NameError:
    print('NameError')

import_3.j = 888
import_3.print_j()