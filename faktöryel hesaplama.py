# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:16:42 2023

@author: senol
"""



def faktoryel(sayi):
    sonuc=1
    for i in range(1,sayi+1):
        sonuc=sonuc*i
    
    return sonuc
    

print(faktoryel((int(input("faktöryel için bir sayi gir : ")))))

