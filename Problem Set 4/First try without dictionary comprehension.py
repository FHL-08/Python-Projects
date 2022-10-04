# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 13:43:28 2021

@author: HP
"""
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    x = hand.copy()
    for letter in word:
        if letter in hand.keys():
            x[letter] = x.get(letter, 0) - 1
        else:
            x[letter] = x.get(letter, 0)
    return x 
   