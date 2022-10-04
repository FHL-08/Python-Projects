# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 16:41:24 2021

@author: Faisal Lawan
"""


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr)==0:
        return False
    
    elif char!=aStr[int(len(aStr)/2)] and len(aStr)>2:
        if char>aStr[int(len(aStr)/2)]:
            return len(aStr)>=1 and isIn(char, aStr[int(len(aStr)/2)+1: ])
        else:
            return len(aStr)>=1 and isIn(char, aStr[ :int(len(aStr)/2)])    
    
    else:
        if len(aStr)==2:
            return char==aStr[0]
        else:
            return char==aStr[int(len(aStr)/2)]
        
        
            
        
                
                
        
