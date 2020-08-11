#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:41:14 2020

@author: pauladkisson
"""

print("in import, before import statement")
print("name =", __name__)
pre_importVar = []
import importedLecture as iL
post_importVar = pre_importVar.copy()
pre_importVar.append(1)
iL.pre_importedVar.append(1)
print("in import, after import statement")


if __name__ == "__main__":
    #Some printing stuff
    print("")
    print("pre_importVar:", pre_importVar)
    print("post_importVar:", post_importVar)
    print("pre_importedVar:", iL.pre_importedVar)
    print("post_importedVar:", iL.post_importedVar)
    print("nested pre_importVar:", iL.il.pre_importVar)
    print("nested post_importVar:", iL.il.post_importVar)
    
    #Double checking understanding
    print("Is pre_importVar the same as nested pre_importVar?")
    print(pre_importVar is iL.il.pre_importVar)
    print("Is post_importVar the same as nested post_importVar?")
    print(post_importVar is iL.il.post_importVar)
    print("Is pre_importedVar the same as nested pre_importedVar?")
    print(iL.pre_importedVar is iL.il.iL.pre_importedVar)
    print("Is post_importedVar the same as nested post_importedVar?")
    print(iL.post_importedVar is iL.il.iL.post_importedVar)
    