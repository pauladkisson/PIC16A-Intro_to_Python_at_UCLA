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
    
    
    
    

#Test Cases
l = LinkedList()
l.append(1)
l.append('r')
l.append({1:1, 2:2})
assert l.first.data == 1, "Error 1"
assert l.first.next.data == 'r', "Error 1.25"
assert l.first.next.next.data == {1:1, 2:2}, "Error 1.5"
assert l.first.next.next.next == None, "Error 1.75"
assert l.last.data == {1:1, 2:2}, "Error 2"
assert l.len == 3, "Error 3"

l.prepend(201)
l.prepend("Your mother was a hamster...")
l.prepend("...and your father smelt of elderberries")
assert l.first.data == "...and your father smelt of elderberries", "Error 4"
assert l.last.data == {1:1, 2:2}, "Error 5"
assert l.len == 6, "Error 6"

L = LinkedList([1, 2, 5, "three, sir"])
assert L.first.data == 1, "Error 7"
assert L.last.data == "three, sir", "Error 8"
assert L.len == 4, "Error 9"

LL = LinkedList()
assert len(LL) == 0, "Error 10"
LL.append({"Blah"})
assert len(LL) == 1, "Error 11"
LL.prepend([{1:1}, {2:2}])
assert len(LL) == 2, "Error 12"

Lempty = LinkedList()
L01 = LinkedList([0])
L02 = LinkedList([0])
L1 = LinkedList([1])
assert (Lempty == L01) == False, "Error 13"
assert (L01 == L02) == True, "Error 14"
assert (L01 == L1) == False, "Error 15"

n1 = Node(8)
n2 = Node([88])
n3 = Node('888')
assert str(n1) == "8", "Error 16"
assert str(n2) == "[88]", "Error 17"
assert str(n3) == "'888'", "Error 18"

LL = LinkedList(['8', [8], [8], '8'])
LL.append(1)
LL.append(2)
LL.append(3)
LL.prepend(-1)
LL.prepend(-2)
LL.prepend(-3)
assert str(LL) == "[-3 -> -2 -> -1 -> '8' -> [8] -> [8] -> '8' -> 1 -> 2 -> 3 -> ]", "Error 19"

LL = LinkedList(['8', [8], [8], '8'])
LL.append(1)
LL.prepend(-1)
assert repr(LL) == "LinkedList([-1, '8', [8], [8], '8', 1])", "Error 20"
LL = LinkedList(['any old shit', {1:1, 2:[3, 4, '5'], 'monty':{1, 2, "python"}}, 'yo', 1232, 'mama', ('just', 'for', "fun")])
assert eval(repr(LL)) == LL, "Error 21"

LL = LinkedList([-3, -2, -1, '8', [8], [8], '8', 1, 2, 3])
LL.insert(0,5)
assert str(LL) == "[-3 -> -2 -> -1 -> '8' -> [8] -> 0 -> [8] -> '8' -> 1 -> 2 -> 3 -> ]", "Error 22"
LL.insert("blah", -1)
assert str(LL) == "[-3 -> -2 -> -1 -> '8' -> [8] -> 0 -> [8] -> '8' -> 1 -> 2 -> 'blah' -> 3 -> ]", "Error 23"
#LL.insert("bllobe", 100) #Should throw an error
#LL.insert("adfj", -100) #Should throw an error
LL.insert("poop", len(LL))
assert str(LL) == "[-3 -> -2 -> -1 -> '8' -> [8] -> 0 -> [8] -> '8' -> 1 -> 2 -> 'blah' -> 3 -> 'poop' -> ]", "Error 24"
LL.insert("chungus", 0)
assert str(LL) == "['chungus' -> -3 -> -2 -> -1 -> '8' -> [8] -> 0 -> [8] -> '8' -> 1 -> 2 -> 'blah' -> 3 -> 'poop' -> ]", "Error 25"

LL = LinkedList(['8', [8], [8], '8'])
LL.append(1)
LL.append(2)
LL.prepend(-1)
LL.prepend(-2)
LL.insert(0,4)
assert len(LL) == 9, "Error 26"
assert str(LL.first) == '-2', "Error 27"
assert str(LL.last) == '2', "Error 28"
assert str(LL) == "[-2 -> -1 -> '8' -> [8] -> 0 -> [8] -> '8' -> 1 -> 2 -> ]", "Error 29"
assert repr(LL) == "LinkedList([-2, -1, '8', [8], 0, [8], '8', 1, 2])", "Error 30"
assert eval(repr(LL)) == LL, "Error 31"




