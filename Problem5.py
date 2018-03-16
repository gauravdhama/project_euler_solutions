# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 16:06:16 2016

@author: e065689
"""

# Problem 5 - Smallest Multiple

x = range(1,11)

def isprime(n):
    i=2
    while True:
        if n%i==0 and not(i==n) or n==1:
            return False
            break
        if i>=n:
            break
        i=i+1
    return True

primes = []
nonprimes = []
prod = 1

for i in x:
    prod = prod*i
    if isprime(i):
        primes.append(i)
    else:
        if not(i==1):
            nonprimes.append(i)

prod_prime=1
for i in primes:
    prod_prime = prod_prime*i

for i in nonprimes:
    if not(prod_prime%i==0):
        temp = prod_prime
        for j in primes:
            temp= temp*j
            if (temp%i==0):
                prod_prime = prod_prime*j
                break

#Check
for i in nonprimes:
    if prod_prime%i==0:
        print i
        print 'yes'

