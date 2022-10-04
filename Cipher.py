# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:55:18 2021

@author: HP
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    
    next_index = 0
    shiftinglist =[]
    key_code = dict({})
    
    
    for i in map_from:
        key_code[i] = map_to[next_index]
        next_index += 1
    
    for x in code:
        shiftinglist.append(x)
    
    for y in range(len(shiftinglist)):
        shiftinglist[y] = key_code[shiftinglist[y]]
        
    return (key_code, "".join(shiftinglist))
    
    
    
    
    
    
    