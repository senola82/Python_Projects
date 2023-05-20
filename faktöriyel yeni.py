# -*- coding: utf-8 -*-
"""
Created on Sat May  6 02:37:18 2023

@author: senol
"""




def factorial(n):

  sonuc=1
  for i in range(1,n+1):      
      sonuc=sonuc*i         
  
  return sonuc

print(factorial(5))