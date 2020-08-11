#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

print('Code in import_2b.py starts executing')
print('__name__ ==', __name__)

if __name__ == '__main__':
    print('')

import import_2a


if __name__ == '__main__':
    print('')
    print('import_2a.var ==', import_2a.var)

print('Code in import_2b.py finishes executing')