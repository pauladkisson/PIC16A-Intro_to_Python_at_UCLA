#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 10, 2020

@author: Paul Adkisson
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt







#%% PART A
barrel = mpimg.imread("barrel.jpg")
jb = mpimg.imread("jb.jpg")
plt.figure()
plt.imshow(barrel)
plt.figure()
plt.imshow(jb)

barrel_center = barrel.shape[0]//2, barrel.shape[1]//2
jb_center = jb.shape[0]//2, jb.shape[1]//2
jb_barrel_A = barrel.copy()
to_be_jb = (barrel_center[0]-jb_center[0], barrel_center[0]+jb_center[0], barrel_center[1]-jb_center[1], barrel_center[1]+jb_center[1])
    
    
try:
    jb_barrel_A[to_be_jb[0]:to_be_jb[1], to_be_jb[2]:to_be_jb[3]] = jb
except ValueError: ##Due to floor division of odd-sized images
    try: #Fix y-coord (shifting slightly to the up of center)
        jb_barrel_A[to_be_jb[0]:to_be_jb[1]+1, to_be_jb[2]:to_be_jb[3]] = jb
    except ValueError: #It's not just the x-coord
        try: #Fix x-coord (shifting slightly right of center)
            jb_barrel_A[to_be_jb[0]:to_be_jb[1], to_be_jb[2]:to_be_jb[3]+1] = jb
        except ValueError: #It's not just the y-coord
            #Fix x and y coords (shifting slightly right and up of center)
            jb_barrel_A[to_be_jb[0]:to_be_jb[1]+1, to_be_jb[2]:to_be_jb[3]+1] = jb

plt.figure()
plt.imshow(jb_barrel_A)
mpimg.imsave("jb_barrel_A.jpg", jb_barrel_A)

plt.close('all')
#%% PART B
jb_barrel_B = barrel.copy()
LEGS_CUTOFF = 400
CIRCLE_TOP = 165

try:
    jb_barrel_B[CIRCLE_TOP:CIRCLE_TOP+LEGS_CUTOFF, to_be_jb[2]:to_be_jb[3]] = jb[:LEGS_CUTOFF]
except ValueError: ##Due to floor division of odd-sized images
    #Fix x-coord (shifting slightly to the right of center)
    jb_barrel_B[CIRCLE_TOP:CIRCLE_TOP+LEGS_CUTOFF, to_be_jb[2]:to_be_jb[3]+1] = jb[:LEGS_CUTOFF]

plt.figure()
plt.imshow(jb_barrel_B)
mpimg.imsave("jb_barrel_B.jpg", jb_barrel_B)

plt.close('all')
#%% PART C
jb_barrel_C = barrel.copy()
print(barrel[650, 1000])
WHITE = 150
circle_mask = barrel > WHITE
jb_barrel_C[circle_mask] = jb_barrel_B[circle_mask]

plt.figure()
plt.imshow(jb_barrel_B)
mpimg.imsave("jb_barrel_C.jpg", jb_barrel_C)

plt.close("all")







