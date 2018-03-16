# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:40:45 2016

@author: e065689
"""

#Problem 6

n = 100

i=1
sumsq = 0
sqsum = 0
while True:
    sumsq = sumsq+i**2
    sqsum = sqsum+i
    if i==n:
        break
    i=i+1

sqsum = sqsum**2

print sqsum-sumsq

