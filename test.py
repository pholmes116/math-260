#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:51:14 2020

@author: PetersMacBook
"""

class Node:
    """ M2: Node class """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
        
    def __repr__(self):
        return "Node({})".format(self.data)



class Chain:
    """ M2: chain class """

    def __init__(self, data):
        self.front_node = Node(data)

    def __repr__(self):
        rep = str(self.front_node.data) + " - "
        
        front = self.front_node.next_node
        
        while front:
            rep += str(front.data) + " - "
            front = front.next_node
        
        return rep

    def pop(self):
        """ remove the element from the front, return its *data* """
        old_front = self.front_node.data
        
        self.front_node = self.front_node.next_node
        
        return old_front

    def prepend(self, data):
        """ insert a new node with the input data
            in front of the chain"
        """
        old_front = self.front_node
        
        self.front_node = Node(data, old_front)
        

    def insert(self, data, k):
        """ insert a new node with the input data
            after the k-th node in the chain
        """
        front = self.front_node
        
        i = 0
        
        while front:
            new = front
            front = front.next_node
            
            if k == i:
                break
            
            i += 1
            
        if k > i:
            print("Error: Entered k-value out of range of length of the chain")
        else:
            new.next_node = Node(data, front)

        
        
def evens(n):
    """ M2: Create the specified chain
        n >= 2 is an integer.
    """
    a = Chain(2)
    k = 0
    
    for data in range(4, (2*n)+1, 2):
        a.insert(data, k)
        k += 1
        
    return a