# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:29:11 2021

@author: HP
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    import string
    
    invalid = string.ascii_lowercase+string.ascii_uppercase+" !@#$%^&*()-_+={}[]|\:;'<>?,./\""
    ans = 0
    count = 0
    for i in s:
        if i in invalid:
            pass
        else:
            ans += int(i)
            count+=1
    if count == 0:
        raise ValueError("There are no digits witthin this string ")
    else:
        return ans
            
    
    
    
            