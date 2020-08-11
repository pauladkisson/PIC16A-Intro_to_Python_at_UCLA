#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday Apr 22 00:00:00 2020

@author: pauladkisson
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self, pythonList = None):
        self.first = None
        self.last = None
        self.len = 0
        if type(pythonList) == list:
            for data in pythonList:
                self.append(data)     

        

    def append(self, data):
        if self.len == 0:
            self.first = Node(data)
            self.last = self.first #It's important that first and last point to the same object!!
            self.len = 1
        else:
            self.last.next = Node(data) #Create new node object and update the old last node's next to point to the new object
            self.last = self.last.next #Update last so that it points to the new node object created in previous line
            self.len += 1
            
    def prepend(self, data):
        if self.len == 0:
            self.first = Node(data)
            self.last = self.first #It's important that first and last point to the same object!!
            self.len = 1
        else:
            newFirst = Node(data) #Create the new first node
            newFirst.next = self.first #Have new first node point to old first node
            self.first = newFirst  #Update first
            self.len += 1

    def __len__(self):
        return self.len
    
    def __eq__(self, other):
        if self.len != other.len:
            return False
        else:
            self_node = self.first
            other_node = other.first
            is_equal = self_node.data == other_node.data
            while(is_equal and self_node.next != None): #If self_node.next = None --> it's the last node
                self_node = self_node.next
                other_node = other_node.next
                is_equal = self_node.data == other_node.data
            return is_equal
        
    def __str__(self):
        node = self.first
        outstring = "[" + str(node) + " -> "
        while(node.next != None): #If node.next == None --> it's the last node
            node = node.next
            outstring += str(node) + " -> "
        outstring += "]"
        return outstring
    
    def __repr__(self):
        node = self.first
        outstring = "LinkedList(["
        while(node.next != None): #If node.next == None --> it's the last node
            outstring += str(node) + ", "
            node = node.next
        outstring += str(node) + "])"
        return outstring
    # 11
    def insert(self, data, idx):
        if abs(idx) > len(self):
            raise IndexError("LinkedList index out of range")
        elif idx == len(self):
            self.append(data)
        elif idx == 0:
            self.prepend(data)
        elif idx < 0: #supporting negative indexing
            idx += len(self)
            self.insert(data, idx)
        else: #Normal (not edge) cases
            node = self.first
            for i in range(idx): #0, ... , idx-1
                if i == idx-1:
                    newNode = Node(data)
                    newNode.next = node.next
                    node.next = newNode
                else:
                    node = node.next
            self.len += 1




