# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:58:30 2021

@author: HP
"""

def genPrimes():
    n=2
    primes = [2]    
    yield primes[0]
    
    while True:
        n += 1
        for p in primes:
            if (n%p) == 0:
                break
        else:
            primes.append(n)
            yield n