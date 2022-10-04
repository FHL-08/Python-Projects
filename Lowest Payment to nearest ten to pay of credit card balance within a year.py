# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:36:27 2021

@author: HP
"""

balance=input("Credit Card Balance: ")
annualInterestRate = input("Bank Annual Interest Rate: ")
month=0

def leastPayment(x, y, p, month, n):
    
    Interest=0
    if x<=0 and month==12:
        return p
    elif month==12 and x>0:
        x=n
        while month<12:
            RemainingBalance=x-p
            Interest=RemainingBalance*y
            x=RemainingBalance+Interest
            month+=1
        return leastPayment(x, y, p+10, 0, n) 
    else:
        while month<12:
            RemainingBalance=x-p
            Interest=RemainingBalance*y
            x=RemainingBalance+Interest
            month+=1
        return leastPayment(x, y, p, month, n) 
        
            
monthlyInterestRate=annualInterestRate/12
Payment=10
print("Lowest Payment: ", leastPayment(balance, monthlyInterestRate, Payment, month, balance))


        
if len(str(balance))>2:
    Payment=int((str(balance))[0])*(10**(len(str(balance))-2))
else:
    Payment=10       
    
    
    
    
