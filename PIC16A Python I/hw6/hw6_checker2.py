#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: mjandr
"""

#%% THE POSSIBLE TRICKS
# #  Name             Number
# -  nothing          1,302,540  # we will not include these
# 0  one pair         1,098,240
# 1  two pair         123,552
# 2  three of a kind  54,912
# 3  straight         10,200
# 4  flush            5,108
# 5  full house       3,744
# 6  four of a kind   624
# -  straight flush   40         # we will not include these

# We specify for each type of trick, 
# how many we'll use for training, 
# and how many we'll use for testing.

# train_size = [8000, 8000, 4500, 850, 425, 300,  50]  # larger training sets
train_size = [ 100,   50,   50, 100, 100,  50,  50]
test__size = [ 100,  100,  100, 800, 800, 100, 100]

#%% IMPORTS
import json
import numpy as np
from hw6 import preprocess
from sklearn.svm import SVC
from itertools import combinations as choose

#%% GENERATING ALL HANDS
cards = range(52)
hands = np.array(list(choose(cards, 5)), dtype = np.int8)

with open('trick.json') as f:
    trick = np.array(json.load(f), dtype = np.int8)

hands = [hands[trick == i] for i in range(1,8)]

# You do not need to worry about how I created hands.
# But you should understand how the data in hands is stored.
# This should help you...
print('hands has type ', type(hands))
print('hands[0] has type ', type(hands[0]), '\n')

# hands[0] consists of one pairs
# hands[1] consists of two pairs
# ...
# hands[5] consists of full houses
# hands[6] consists of four of a kinds

print('     one pairs:', hands[0][280004], hands[0][280005])
print('     two pairs:', hands[1][ 80004], hands[1][ 80005])
print('    full house:', hands[5][888])
print('four of a kind:', hands[6][ 88])
print('')

#%% PARTITION HANDS INTO TRAINING AND TESTING SETS AND CREATE TARGETS
def partition(h, train, test):
    l = len(h)
    p = np.random.permutation(l)
    h = h[p]

    assert train > 0 and test > 0 and train + test <= l
    return h[:train], h[-test:]

N = len(hands)

samples = [partition(hands[i], train_size[i], test__size[i]) for i in range(N)]

train_samples = np.concatenate( [samples[i][0] for i in range(N)] )
test__samples = np.concatenate( [samples[i][1] for i in range(N)] )

train_targets = np.array([i for i in range(N) 
                            for _ in range(train_size[i])], dtype = np.int8)
test__targets = np.array([i for i in range(N) 
                            for _ in range(test__size[i])], dtype = np.int8)

#%% TRAIN THE SVC AND TEST ITS ACCURACY
clf = SVC(kernel = 'linear')
clf.fit(preprocess(train_samples), train_targets)

predict = clf.predict(preprocess(test__samples))
correct = test__targets

#####
#Checking things myself -- delete later
import matplotlib.pyplot as plt
trans_samples = preprocess(train_samples)
pairs = train_targets == 0
two_pairs = train_targets == 1
three_o_kinds = train_targets == 2
straights = train_targets == 3
flushes = train_targets == 4
full_houses = train_targets == 5
four_o_kinds = train_targets == 6

f = plt.figure()
plt.scatter(trans_samples[full_houses][:, 0], trans_samples[full_houses][:, 1], c = "red")
plt.scatter(trans_samples[four_o_kinds][:, 0], trans_samples[four_o_kinds][:, 1], c = "blue")
plt.scatter(trans_samples[straights][:, 0], trans_samples[straights][:, 1], c = "green")
plt.scatter(trans_samples[pairs][:, 0], trans_samples[pairs][:, 1], c = "purple")
plt.scatter(trans_samples[two_pairs][:, 0], trans_samples[two_pairs][:, 1], c = "black")
plt.scatter(trans_samples[three_o_kinds][:, 0], trans_samples[three_o_kinds][:, 1], c = "yellow")
plt.scatter(trans_samples[flushes][:, 0], trans_samples[flushes][:, 1], c = "grey")
####

print('accuracy ==')
print(100 * np.count_nonzero(predict == correct) / len(correct))

# SHOW INFO ABOUT WRONG PREDICTIONS
# print(test__samples[predict != correct])
# print(correct[predict != correct], predict[predict != correct])