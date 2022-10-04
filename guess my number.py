# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:59:11 2021

@author: HP
"""

print("Please think of a number between 0 and 100!")
high=100
low=0
guess=int((high+low)/2)
info=""
while info.lower() != "c":
    print("Is your secret number", guess, "?")
    info=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if info.lower() == "h":
        high=guess
        guess=int((high+low)/2)
    elif info.lower() == "l":
        low=guess
        guess=int((high+low)/2)
    else:
        if info.lower() == "c":
            break
        print("Sorry, I did not understand your input.")

print("Game Over.", end=" ")    
print("Your secret number was:", guess)
