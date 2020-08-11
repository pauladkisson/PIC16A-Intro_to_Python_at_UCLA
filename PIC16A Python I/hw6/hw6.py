#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/14/2020

@author: Paul Adkisson
"""

import numpy as np

#%% PREPROCESSING
def preprocess(data):
    #Var1 = number of times that the numbers (A, 2, 3, ..., K) are equal
    number = data % 13
    Var1 = np.zeros((number.shape[0]), dtype = np.uint8)
    for card1 in range(5):
        for card2 in range(card1+1, 5):
            Var1 += (number[:, card1] == number[:, card2])
    
    #Var2 = number of times that the suits (Clubs, Diamons, Hearts, Spades) are equal
    suit = np.floor(data/13)
    Var2 = np.zeros((number.shape[0]), dtype = np.uint8)
    for card1 in range(5):
        for card2 in range(card1+1, 5):
            Var2 += (suit[:, card1] == suit[:, card2])

    output = np.concatenate((Var1[:, np.newaxis], Var2[:, np.newaxis]), axis = 1)
    return output