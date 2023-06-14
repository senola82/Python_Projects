# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 01:35:09 2023

@author: senol
"""

liste=["e","b","se3","ss33","sdfsf4","asd55","1se"]

sayac=len(liste)

for i in liste:
        
    print(liste.__getitem__((sayac-1)))
    sayac-=1
    
    
for i in range(len(liste)):
    print(liste[len(liste)-i-1])
    
    

for index ,item in enumerate(liste):
    print(liste[len(liste)-index-1])
    
    
    
ii=-1
for i in liste:
    print(liste[ii])
    ii-=1
      
    
    
    
    
#print("ss33"  in liste)