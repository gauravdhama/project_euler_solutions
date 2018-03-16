# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 20:43:53 2016

@author: e065689
"""

# Collatz Sequence Generator


j = 1000000
jl = 0
largest = 0

while j>2:
    n = j
    c = 0
    while n>1:
        if n%2 == 0:
            n = n/2            
            c = c+1
        elif n%2 == 1:
            n = 3*n+1
            c = c+1
    if c>largest:
        largest=c
        jl = j
        print jl
        print largest
    j = j-1
        