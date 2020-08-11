#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:15:04 2020

@author: pauladkisson
"""


try:
    try:
        print('0')
        raise ZeroDivisionError
        print('1')
    except:
        print('2')
        raise
        print('3')
        
    print('4')
    
except ZeroDivisionError:
    try:
        print('5')
        raise ZeroDivisionError
        print('6')
    except:
        print('7')
        
    print('8')
    raise NameError
except NameError:
        print('9')
    
print('10')