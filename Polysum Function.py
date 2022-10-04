# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 21:29:14 2021

@author: HP
"""

from math import *

def polysum(n, s):
   """
   n: positive integer, Number of sides of polygon
   s: positive integer, Length of sides of polygon
   
   """
   a = ((0.25*n*(s**2))/tan(pi/n))
   p = n*s
   return round(a+(p**2), 4)