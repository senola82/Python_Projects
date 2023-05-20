# -*- coding: utf-8 -*-
"""
Created on Sat May  6 02:17:33 2023

@author: senol
"""


def max_list(a):
    yeni = a[0] # listenin ilk elemanını en büyük sayı olarak varsay
    for i in range(len(a)): # listenin tüm elemanlarını dolaş
        if a[i] > yeni: # eğer bir eleman yeni'den büyükse
            yeni = a[i] # yeni'yi o eleman yap
    return yeni # en büyük sayıyı döndür

liste = [20,10,5,3,88,5]
print(max_list(liste))