# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:55:07 2016

@author: e065689
"""
import math
#Prime Factors

def isprime(n):
    i=2
    while True:
        if n%i==0 and not(i==n):
            return False
            break
        if i>=n:
            break
        i=i+1
    return True

n = 60085147514313195

while (n%2==0):
    n = n/2

i = 3
largest = 2

while True:
    if isprime(i) and n%i==0:
        largest = i
        print largest
        n = n/i
    if i>=math.sqrt(n):
        break
    i = i+2

if n>2 and isprime(n):
    largest=n

print "Final Value : "+str(largest)