#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:06:29 2020

@author: pauladkisson
"""
import hw4

def testing():
    output = ""
    def f1():
        r = hw4.Rectangle(2.0, 4.0)
        del r['len1']

    def f2():
        r = hw4.Rectangle(2.0, 4.0)
        r['len1'] = 2

    def f3():
        r = hw4.Rectangle(2, '4')
        return r

    def f4():
        class C(hw4.StructuredDict):
            key_to_type = {0:int, 1:int, 2:int, 3:float, 4:str}

        c = C({2:2, 3:3, 4:4, 5:5, 6:6})
        return c
    
    def f5():
        s = hw4.Student("Billy", "Jenkins", 3.7)
        s["GPA"] = "blah"
    def f6():
        s = hw4.Student("Billy", "Jenkins", 3.7)
        del s["GPA"]
    def f7():
        s = hw4.Student(1, {2}, "blah")
        
    L = [f1, f2, f3, f4, f5, f6, f7]

    for f in L:
        try:
            output += "\n"
            f()
        except hw4.DeleteError as e:
            output += 'DeleteError:' + " " + str(e)
        except hw4.UpdateValueError as e:
            output += 'UpdateValueError:' + " " + str(e)
        except hw4.InitializationError as e:
            output += 'InitializationError:' + " " + str(e)
    
    return output

print(testing())
    
class myError(Exception):
    def __str__(self):
        return "I made my own error"

try:
    raise myError
except myError as e:
    print("myError: %s" %e)
