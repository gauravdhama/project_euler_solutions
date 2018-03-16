# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 19:31:00 2016

@author: e065689
"""

n = input()
sum1 = 0
val = 1
while True:
    if val%3==0 or val%5==0:
        sum1=sum1+val
    val = val+1
    if val==n:
        break

print sum1