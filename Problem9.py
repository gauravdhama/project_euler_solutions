# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 20:04:53 2016

@author: e065689
"""

# Problem 9
a = 0
b = 0
c = 0

for x in range (1, 1000):
    for y in range (x+1, 1000):
        for z in range(y+1, 1000):
            if x*x + y*y == z*z:
                print x, y, z
                if (x+y+z)==1000:
                    a=x
                    b=y
                    c=z

print a*b*c