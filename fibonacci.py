# -*- coding: utf-8 -*-
"""
Created on Sat May  6 02:54:15 2023

@author: senol
"""

def fibonacci(n):
    a=1    
    b=0
    sonuc=0
    for i in range(0,n+1):
        
        sonuc=a+b      
        b=a
        a=sonuc
        
    return sonuc


print(fibonacci(6))