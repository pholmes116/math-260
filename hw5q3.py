#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: More on Markov Chains and Bees
@author: Peter Holmes
"""

import numpy as np
from numpy.random import uniform

### Part a (optional)

def escape_chance(steps):
    
    p = np.array([[0.5, 0.4, 0.0, 0.1],
                  [0.5, 0.0, 0.5, 0.0],
                  [0.7, 0.3, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
    
    pt = p.transpose()
    
    x0 = np.array([[0],
                   [1],
                   [0],
                   [0]])   
    
    for i in range(steps):
        xk = pt.dot(x0)     
        x0 = xk
        
    escape_prob = xk[-1][0]    
    
    return escape_prob
    
""" 
To be 99% sure that the bee is gone, you should stay out of the house for
between 80 and 81 minutes. 
"""

### Part b (optional)

def choose(probs):
    """ Example code (from lecture, edited) to pick a choice.
        given choices 0, ..., n-1 with probs p0, .. p_(n-1),
        picks one with the appropriate probability.
    """
    r = uniform(0, 1)
    total = probs[0]
    k = 0
    while r > total:
        k += 1
        total += probs[k]
    return k


def release_the_bees(nb, steps):  # for closed part
    p = np.array([[0.5, 0.5, 0.0],
                  [0.5, 0.0, 0.5],
                  [0.7, 0.3, 0]])  # the transition matrix
    
    b_dist = np.array([[nb, 0, 0]])
    b_new = np.array([[0, 0, 0]])
    
    for i in range(steps):
        for j in range(3):
            for x in range(b_dist[0][j]):
                k = choose(p[j])
                
                b_new[0][k] += 1 
                
        b_dist = b_new
        b_new = np.array([[0, 0, 0]])       
        
    return b_dist

def avg(n):
    """ 
    Runs release_the_bees() with 1000 bees and 500 steps, 'n' times and returns 
    numpy array of the average stationary distribution
    """
    total = release_the_bees(1000, 500)
    
    for i in range(n-1):
        print(i+1)
        total += release_the_bees(1000, 500)
        
    mean = total / n
    
    return mean

"""
After funning avg(100) I got the stationary distribution of
[ 530.64,  313.25,  156.11] which with 1000 bees results in nearly the same as 
the theory of s ~ (.531, .313, .156)
"""
