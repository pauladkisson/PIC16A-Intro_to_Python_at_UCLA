#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:42:16 2020

@author: pauladkisson
"""
print("in imported, before import statement")
print("name =", __name__)
pre_importedVar = []
import importLecture as il
post_importedVar = pre_importedVar.copy()
pre_importedVar.append(2)
il.pre_importVar.append(2)
print("in imported, after import statement")
