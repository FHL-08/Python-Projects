# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:44:53 2021

@author: HP
"""
s="aabcbcd"
check=0
num=(len(s)+1)
mylist=[]
for letter in s:
    long=""
    long+=letter
    for i in range(num+check):
         print(s[(i+check+1)])
               
    check+=1         
    mylist.append(long)
    

 if s[(i+check+1)] >=s [i+check]:
             long+=s[(i+check+1)]
else:
             mylist.append(long)
             break  
 
        
            
            

           
         
             
              
                    