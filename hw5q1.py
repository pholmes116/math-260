#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Solving ODEs
@author: Peters Holmes
"""

### Part a

""" 
Because 'K' is defined as the maximum value of the population, the value of the 
curent value of the population 'p' must be less than 'K' and therefore
'p/K' is greater than 0 and less than 1
"""

### Part b

def fwd_back_euler(r, y0, t0, t1, h = 1e-3):
    
    if t1 < t0:
        h *= -1
    
    def f(r, y):
        return r * y * (1 - y)
    
    y = y0
    t = t0
    
    while abs(t - t1) > 1e-12:
        y += h * f(r, y)
        t += h      
        
    return y

### Part c

import matplotlib.pyplot as plt
import numpy as np

def rk4(r, y0, t0, t1, h = 1e-3):
    
    if t1 < t0:
        h *= -1
        
    def f(r, y):
        return r * y * (1 - y)
    
    y = y0
    t = t0
    
    yvals = [y]
    tvals = [t]
    
    while abs(t - t1) > 1e-12:
        f1 = f(r, y)
        f2 = f(r, y + (h / 2) * f1)
        f3 = f(r, y + (h / 2) * f2)
        f4 = f(r, y + h * f3)
        
        y += (h / 6) * (f1 + (2 * f2) + (2 * f3) + f4)
        t += h
        
        yvals.append(y)
        tvals.append(t)
    
    return yvals, tvals


def exact(t):
    return 1 / (1 + np.e ** (-t))


y, t = rk4(1, 0.5, 0, 5)

exact_list = [exact(x) for x in t]

plt.figure()
plt.plot(t, y, '-b', t, exact_list, '-r')
plt.legend(["approx", "exact"])
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.show

### Part d (optional)

def max_error(h):
    y, t = rk4(1, 0.5, 0, 5, h)
    
    new_exact = [exact(x) for x in t]
    
    errors = [abs(new_exact[i] - y[i]) for i in range(len(y))]
    
    return max(errors)

### Part e (optional)

k = 10
hvals = [2 ** (-i) for i in range(1, k+1)]
max_e = [max_error(h) for h in hvals]

plt.figure()
plt.loglog(hvals, max_e, '.--b')
plt.xlabel('$h$')
plt.ylabel('$E(h)$')
plt.show()

"""
From looking at the resulting plot of max-error vs. step, we can see that the
slope is correct (order = 4), and to get a max error of ~ 10e-6 we can have an
h of ~.5. 

Compared to Euler's method this is much better, as we would need an h of ~.001
"""
