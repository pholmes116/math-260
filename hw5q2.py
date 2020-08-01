#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Page Rank
@author: Peter Holmes
"""

import numpy as np
from scipy import sparse
import pagerank as pr

### Part a

def pr_matrix(fname, alpha):
    adj, n, names = pr.read_graph_file(fname)
    
    p = np.zeros([n, n])
    
    for j in range(n):
        for x in range(len(adj[j])):
            
            neighbors = len(adj[j])
            k = adj[j][x]
            
            p[j][k] = 1 / neighbors
            
    m = alpha * p.transpose() + ((1 - alpha) / n) * np.ones([n, n]) # or is it just divided by 4 not n?
        
    return m


def node_rank(alpha):
    adj, n, names = pr.read_graph_file('small_graph.txt')
    m = pr_matrix('small_graph.txt', alpha)
    
    dist = pr.ranking(m, 50)
    index_order = dist.argsort()   
    true_order = index_order[::-1]
    
    print("The nodes in ranked order (descending) are:\n")
    
    for i in range(len(true_order)):
        name = names[true_order[i]]
        print("{}".format(name))
    

### Part b (optional)

""" Sparse matrix info read and example code on scipy.org understood """

### Part c (optional)


