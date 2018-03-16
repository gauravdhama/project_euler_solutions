# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:35:05 2016

@author: e065689
"""

n = 10001

def isprime(x):
    i=2
    while True:
        if x%i==0 and not(i==x):
            return False
            break
        if i>=x:
            break
        i=i+1
    return True

i = 2
j = 0
while True:
    if isprime(i):
        j = j+1
    i = i+1
    if j==n:
        print i-1
        break
    