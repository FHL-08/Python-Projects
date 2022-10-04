# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:44:53 2021

@author: HP
"""
s=input("Enter any random combination of letters: ")
mylist=[]
long=""
check=1
for i in range(len(s)):
    if check<len(s):
        if s[check]>=s[i]:
            check+=1
            long+=s[i]
        else:
            check+=1
            long+=s[i]
            mylist.append(long)
            long=""    
    else:
        if s[len(s)-1]>=s[i]:
            long+=s[len(s)-1]
        break 
mylist.append(long)
list2=[]
for char in mylist:
    len(char)
    list2.append(len(char))
largest=max(list2)
ans=list2.index(largest)    
print(mylist[ans])

   

        
            
            

           
         
             
              
                    