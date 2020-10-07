# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 08:47:13 2020

@author: vinic
"""

enters = [7, 13, 5]
weights = [0.8, 0.1, 0.3]

def sum1(e, w):
    s = 0
    for i in range(3):
       #print(enters[i])
       #print(weights[i]) just for test
        s += e[i] * w[i]
    return s
s = sum1(enters, weights)
def stepfunction(sum1):
    if(sum1 >= 1):
        return 1
    return 0

result = stepfunction(s)
