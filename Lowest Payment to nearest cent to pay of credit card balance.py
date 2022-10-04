# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:35:29 2021

@author: HP
"""
balance = int(input("Credit Card Balance: "))
annualInterestRate = int(input("Bank Annual Interest Rate: "))

def LowestPayment(b, m, lb, ub, p, n, month):
    
    if b<=0 and b>(-0.01):
        return p
    
    else:
        b=n
        while month<12:
            RemainingBalance=b-p
            Interest=RemainingBalance*m
            b=RemainingBalance+Interest
            month+=1 
        if b>0:
            lb=p
        else:
            ub=p
        return LowestPayment(b, m, lb, ub, (ub+lb)/2, n, 0)


monthlyInterestRate=annualInterestRate/12
lowerbound=balance/12
upperbound=(balance*((1+monthlyInterestRate)**12))/12
power=(lowerbound+upperbound)/2
month=0


print(round(LowestPayment(balance, monthlyInterestRate, lowerbound, upperbound, power, balance, month), 2))
