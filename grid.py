#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:21:30 2020

@author: PetersMacBook
"""


#Needs:
#grid.nodes as list containing all nodes
#grid.size as number of nodes. or just len(grid.nodes)
#node.adj as list of what is adjacent to 
#node.dist as list of distances correlating to adjacency list

# Adjascency List representation in Python

from random import randint
from string import ascii_uppercase

caps = ascii_uppercase

class Grid:
    def __init__(self, num):
        keys = [caps[i] for i in range(num)]
        dicts = {}
        for i in keys:
            dicts[i] = {"adj": [], "dist": []}
             
        self.dict = dicts
        
        
    def nodes(self):
        node_list = []
        for key in self.dict.keys():
            node_list.append(key)
            
        return node_list
    
    
    def size(self):
        return len(self.dict)
        
    
    def edge(self, node1, node2, distance = None):
        if distance == None:
            distance = randint(0, 9)
        
        d = self.dict
     
        if node1 in d and node2 in d and node1 != node2:      
            d[node1]['adj'].append(node2)
            d[node1]['dist'].append(distance)
            
            d[node2]['adj'].append(node1)
            d[node2]['dist'].append(distance)
        else:
            raise KeyError("Input names of two different existing nodes")
      
        
    def adj(self, node):
        return self.dict[node]['adj']
    
    
    def dist(self, node):
        return self.dict[node]['dist']
    
    def __repr__(self):
        rep = ""
        
        for key in self.dict:
            rep += f"\n{key}: {self.dict[key]}"
        
        return rep

  
if __name__ == "__main__":
    g = Grid(5)
    g.edge('A', 'B', 3)
    g.edge('A', 'C', 7)
    g.edge('A', 'E', 2)
    g.edge('B', 'C', 5)
    g.edge('B', 'D', 9)
    g.edge('B', 'E', 8)
    print(g)


