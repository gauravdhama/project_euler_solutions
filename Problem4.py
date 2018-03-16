# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:54:33 2016

@author: e065689
"""

#Problem 4 - Palindrome Problem

x = range(100,1000)
y = range(100,1000)

x.reverse()
y.reverse()
largest = 0
for v1 in x:
    for v2 in y:
        x = v1*v2
        z = str(x)
        if z==z[::-1] and x>largest:
            largest = x
            print v1
            print v2
            print x