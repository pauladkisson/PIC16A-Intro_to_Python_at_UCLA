#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

# This example has t4 import i4 which itself imports t4.
# This example allows you to follow the exact order of imports, and
# it demonstrates the functionality of __name__ explicity.

# Run t4.py rather than this file; it's more interesting that way.
# Refresh the console after each run.


if __name__ != '__main__':

    print('0  :  i4.py is executing; ', '__name__ ==', __name__, '*** init v')
    v = 88  # Creates a variable called v in the namespace i4.


print('1  :  i4.py is executing; ', '__name__ ==', __name__)
import t4
print('2  :  i4.py is executing; ', '__name__ ==', __name__)



if __name__ == '__main__':
    print(t4)