#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:18:56 2020

@author: pauladkisson
"""

#%% 1
# maybe write another function here...

#Version that I submitted for hw (contains an error)
def longest_path_length(d):
    """Returns the length of the longest path in d."""
    max_path_length = 0
    for key in d:
        path = [(key, d[key])]
        while path[-1][1] in d.keys():
            path.append((path[-1][1], d[path[-1][1]]))
            path_length = len(path)
            #If there are any duplicate tuples --> break the loop --> true length is recorded length - 1    
            if len(set(path)) != path_length:
                path_length -= 1
                break
        if path_length > max_path_length:
            max_path_length = path_length
            
    return max_path_length

#Fixed version (accounts for case where the max path length is 1)
#ex. d = {1:1, 2:2, 3:3}
def longest_path_length(d):
    """Returns the length of the longest path in d."""
    max_path_length = 0
    for key in d:
        path = [(key, d[key])]
        path_length = len(path)
        while path[-1][1] in d.keys():
            path.append((path[-1][1], d[path[-1][1]]))
            path_length = len(path)
            #If there are any duplicate tuples --> break the loop --> true length is recorded length - 1    
            if len(set(path)) != path_length:
                path_length -= 1
                break
        if path_length > max_path_length:
            max_path_length = path_length
            
    return max_path_length
#%% 2
def large_value_keys(d, N):
    """Returns a list containing various keys in d.
    
    d is a dictionary who values are ints. N is an int.
    The list contains keys k whose corresponding value d[k] is bigger than N.
    The keys are arranged in order of largest value to smallest value.
    """
    returnList = []
    dictList = list(d.items())
    dictList.sort(key = lambda x: -x[1])
    keys = [entry[0] for entry in dictList]
    for key in keys:
        if d[key] > N:
            returnList.append(key)
    return returnList
#%% 3
def replace_it(s, *toBeReplaced):
    for item in toBeReplaced:
        s = s.replace(item, ' ')
    return s
    
def count_words(filename):
    """Creates a dictionary from a .txt file counting word occurrences.
    
    For each word in the text file, there's a key.
    The corresponding value is the number of occurrences of the word.
    
    https://docs.python.org/3.7/library/stdtypes.html#string-methods
    
    Capitals are converted to lower case
    so that 'The' does not show up as a key.
    
    Dashes are replaced with spaces
    so that 'them—at' does not show up as a key.
    Both the short dash (-) and long dash (—) are dealt with.
    
    Non-alphabetic characters are stripped from words
    so that '“espionage?”' does not show up as a key.
    However, both "paper’s" and "papers" can show up as keys.
    """

    with open(filename, encoding='utf-8') as f:
        novel = f.read()
    novel = novel.casefold()
    novel = replace_it(novel, '--', '-', ' \'', '\' ', ' "', '" ', '.', ',', '<', '>', '?' '/', ';', ':', ']', '[', 
                       '{', '}', '\\', '|', '=', '+', '_', ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', '~', '`',
                       ' ‘', '‘ ', ' ’', '’ ', '\n', '\t')
    words = novel.split(' ')
    while '' in words:
        words.remove('')
    uniqueWords = set(words)
    d = {word:words.count(word) for word in uniqueWords}
    return d









