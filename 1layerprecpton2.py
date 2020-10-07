# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:27:03 2020

@author: vinic
"""
import numpy as np

enters = np.array([7, 13, 5])
weights = np.array([0.8, 0.1, 0.3])

def sum1(e, w):
    return e.dot(w) #.dot = dot product
s = sum1(enters, weights)

def stepfunction(sum1):
    if(sum1 >= 1):
        return 1
    return 0

result = stepfunction(s)