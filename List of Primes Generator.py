# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:43:28 2021

@author: HP
"""

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    primes = []
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
                
    for n in genPrimes():
        if n <= N:
            primes.append(n)
        else:
            break
    
    return primes
  
    
