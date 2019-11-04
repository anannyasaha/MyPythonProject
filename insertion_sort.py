# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:28:44 2018

@author: Anannya
"""

def sort(list1):
    
    for j in range(1,len(list1)):
       key=list1[j] 
       i=j-1
       while(i>=0 and list1[i]>key):
           list1[i+1]=list1[i]
           i=i-1
       list1[i+1]=key
    return list1
print(sort([5,4,3,2,1]))
       