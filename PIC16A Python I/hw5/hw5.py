#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 6 2020
HW 5
@author: Paul Adkisson
"""

#%%
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#%% Q1
a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')
row_start = int(np.shape(a)[0]/2 - np.shape(b)[0]/2)
row_end = int(np.shape(a)[0]/2 + np.shape(b)[0]/2)
col_start = int(np.shape(a)[1]/2 - np.shape(b)[1]/2)
col_end = int(np.shape(a)[1]/2 + np.shape(b)[1]/2)
c = a.copy()
c[row_start:row_end, col_start:col_end, :] = b
mpimg.imsave('c.jpg', c)

#%% Q2
d = mpimg.imread('d.jpg')
e = mpimg.imread('e.jpg')
f = np.uint8(np.abs(np.int32(d) - np.int32(e)))
mpimg.imsave('f.jpg', f)

#%% Q3
minion = mpimg.imread('g.jpg')
shugga = mpimg.imread('h.jpg')

#Set Background to black
my_minion = np.copy(minion)
my_minion_red = my_minion[..., 0]
my_minion_green = my_minion[..., 1]
my_minion_blue = my_minion[..., 2]
threshold = np.array([125, 130,  125])
mask = (my_minion_red < threshold[0]) & (my_minion_green > threshold[1]) & (my_minion_blue < threshold[2])
my_minion[mask] = 0

#insert minion
i = np.copy(shugga)
minion_shape = np.shape(my_minion)
shugga_shape = np.shape(shugga)
shape_diff = shugga_shape[0] - minion_shape[0]
minion_view = i[shape_diff:, int(shugga_shape[1]/2 - minion_shape[1]/2):int(shugga_shape[1]/2 + minion_shape[1]/2)]
minion_view[np.logical_not(mask)] = my_minion[np.logical_not(mask)]

mpimg.imsave('i.jpg', i)