# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:09:53 2023

@author: senol
"""

# ARA DEĞER TEOREMİ polinom HESAPLAMASI 

#import math

import math
e = math.e
pi = math.pi
cos=math.cos


print("f(xz)*f(x2)<0 ifadesini kontrol et")
print("ÖNCE KÖKÜN VARLIĞINI KONTROL ET")

def polinomhesapla(x):
    #return ((x**3)-2*(x**2))-5
    return pow(e,-x)-cos(x)

n=0

a=float(input("Birinci Sayıyı girin ="))
b=float(input("İkinci Sayıyı girin ="))
c=0
sayac=int(input("iterasyon(döngü Sayısı) girin ="))

print("n", "     X1", "         X2", "         X3", "          f(X1)","       f(X2)", "        f(X3)")
while True:
    
    c=(a+b)/2
    pa=polinomhesapla(a)
    pb=polinomhesapla(b)
    pc=polinomhesapla(c)
    
    print(n+1, "%.7f   " % a, "%.7f   " % b, "%.7f   " % c, "%.7f   " % pa,"%.7f   " % pb,"%.7f   " % pc)
   
    if pa*pc<0:
        b=c
    if pa*pc>0:
        a=c
    sayac-=1

    n+=1;

    if sayac==0:
        
        break