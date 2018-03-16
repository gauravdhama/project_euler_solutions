# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 20:56:15 2016

@author: e065689
"""

def isprime(n):
    i=2
    while True:
        if n%i==0 and not(i==n):
            return False
            break
        if i>=n/2:
            break
        i=i+1
    return True

nmax = 200000

i = 2
mysum = 0

while i<nmax:
    if isprime(i):
        mysum = mysum+i
        print i
    i+=1

print mysum