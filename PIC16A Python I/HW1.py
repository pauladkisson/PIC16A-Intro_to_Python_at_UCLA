#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:36:23 2020

@author: pauladkisson
"""

#%% 1A
def compare_val_w_idx(L):
    """Compares each value of a list of numbers with its index...
    
    L is unaffected by the function call. 
    The function returns a list M of the same length as L.
    
    M[i] is  1 when L[i] is bigger than i, 
    M[i] is -1 when L[i] is  less  than i, 
    M[i] is  0 when L[i] is  equal  to  i.
    """
    M = L.copy()
    for i in range(len(L)):
        if L[i] > i:
            M[i] = 1
        elif L[i] < i:
            M[i] = -1
        else:
            M[i] = 0
    
    return M
#%% 1B
def compare_val_w_idx_no_obj(L):
    """Compares each value of a list of numbers with its index...
    
    No new objects (except ints) are created during the function call!! 
    None is returned, but L is mutated by the function call.
    
    For any list of numbers L, 
    the following code results in True being printed.
    
    M = compare_val_w_idx(L)
    compare_val_w_idx_no_obj(L)
    print(L == M)
    
    So L is mutated to the return value of compare_val_w_idx(L).
    """
    for i in range(len(L)):
        if L[i] > i:
            L.pop(i)
            L.insert(i, 1)
        elif L[i] < i:
            L.pop(i)
            L.insert(i, -1)
        else:
            L.pop(i)
            L.insert(i, 0)
#%% 2A
def keep_first_occurrences(L):
    """Deletes duplicates in a list of numbers.
    
    L is unaffected by the function call. 
    The function returns a list M.
    
    M consists of the same numbers as in L in the same order. 
    However, all but the first occurrence of each number has been deleted.
    """
    M = L.copy()
    M.reverse()
    i = 0
    while i < len(M):
        if M.count(M[i]) > 1:
            M.pop(i)
        else:
            i += 1
    M.reverse()
    return M
#%% 2B
def first_minus_second_no_obj(L1, L2):
    """Removes elements of one list in accordance with another.
    
    No new objects (except ints) are created during the function call!! 
    None is returned, and L2 is unaffected by the function call, 
    but L1 is mutated by the function call.
    
    At the end of the function call, 
    all elements of L1 that occur in L2 have been removed. 
    The remaining elements are left in their original order.
    """
    for i in range(len(L2)):
        while L2[i] in L1:
            L1.remove(L2[i])
#%% 2C
def keep_last_occurrences_no_obj(L):
    """Deletes duplicates in a list of numbers.
    
    No new objects (except ints) are created during the function call!! 
    None is returned, but L is mutated by the function call.
    
    At the end of the function call, 
    L consists of the same numbers as it began with in the same order. 
    However, all but the last occurrence of each number has been deleted.
    """
    i = 0
    while i < len(L):
        if L.count(L[i]) > 1:
            L.remove(L[i])
        else:
            i += 1
#%% 2D
def keep_first_occurrences_no_obj(L):
    """Deletes duplicates in a list of numbers.
    
    No new objects (except ints) are created during the function call!! 
    None is returned, but L is mutated by the function call.
    
    At the end of the function call, 
    L consists of the same numbers as it began with in the same order. 
    However, all but the first occurrence of each number has been deleted.
    """
    L.reverse()
    i = 0
    while i < len(L):
        if L.count(L[i]) > 1:
            L.remove(L[i])
        else:
            i += 1
    L.reverse()
#%% 3
def primes(N):
    """Returns a list of the first N prime numbers.
    
    Receives an int N bigger than or equal to 0, 
    and does what it says above.
    """
    L = []
    num = 1
    while len(L) < N:
        isprime = True
        num += 1
        for j in range(2, num):
            if num % j == 0:
                isprime = False
                break
            else:
                continue 
        if isprime:
            L.append(num)
    return L
