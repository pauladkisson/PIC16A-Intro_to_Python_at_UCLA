#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

print('Code in import_1.py starts executing')
print('__name__ ==', __name__)

L = []

def f():
    L.append('Appended by f defined in import_1.py')


if __name__ == '__main__':
    print('')
    print("Only executes when __name__ == '__main__'")

print('Code in import_1.py finishes executing')