# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:06:51 2017

@author: e065689
"""

n = 100

def fact(x):
    if x<=1:
        return 1
    else:
        return x*fact(x-1)

print fact(n)

s = str(fact(n))

sum1 = 0
for item in s:
    sum1 = sum1+int(item)

print sum1