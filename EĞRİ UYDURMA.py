# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:32:57 2023

@author: senol
"""

# numpy kütüphanesini içe aktar.
import numpy as np

# veri setlerini numpy dizisi olarak tanımla

x = np.array([-2, 0, 2,4,6])
y = np.array([8, -6, -12,10,0])

n = len(x)

a = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - a*np.sum(x))/n
r = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/np.sqrt((n*np.sum(x**2) - (np.sum(x))**2)*(n*np.sum(y**2) - (np.sum(y))**2))



print(
"""FORMÜL
--------------
  
y=ax + b  biçimindeki lineer yaklaşımı bulamak

n=eleman sayısı

-------------------------------------------------------
|        N  * sum(xi*yi)  -  sum(xi) * sum(yi)         |                                                                            
|  a = ------------------------------------------      |
|       N  *  sum(xi^2)  - (sum(xi))^2                 |       
|                                                      |
|                                                      |
|        sum(xi^2) *sum(yi) - sum(xi) * sum(xi*yi)     |
|  b = -------------------------------------------     |
|           N  *  sum(xi^2)  - (sum(xi))^2             |
|                                                      |
------------------------------------------------------- 

""")



print("---------------------------------TABLO OLUŞTURMA---------------------------------")

print("xi",end="    | ")       
for i in x:
    print("%.2f" % i,end=", ")
print("             | ",sum(x))
print("----------------------------------------------------------------------------------------------")
print("yi",end="    | ")     
for i in y:
    print("%.4f" % i,end=", ")
print("   | ",sum(y))
print("----------------------------------------------------------------------------------------------")
print("xi^2",end="  | ")     
for i in range(0,len(x)):
    print("%.4f" % x[i]**2,end=", ")
print("   | ",sum(x**2))
print("----------------------------------------------------------------------------------------------")
print("xi*yi",end=" | ")     
for i in range(0,len(x)):
    print("%.4f" % float(x[i]*y[i]),end=", ")
print("   | ","%.4f"%sum(x*y))
print("----------------------------------------------------------------------------------------------",end="\n\n")

print ("---------------------------------FORMULDE YERİNE YAZMA----------------------------------")


print("    ",n,"*  %.4f" %(sum(x*y)),"-   %.4f" % sum(x),"*  %.4f" %sum(y))

print("a = -----------------------------------",end=" ")
print("= %.4f   " %a)

print("    ",n,"*  %.4f " %(sum(x**2)),"-  %.4f " %sum(x),"^2")


print("")

print("    %.4f" %(sum(x**2))," *  %.4f" % (sum(y)),"-  %.4f" %(sum(x)),"*  %.4f" %(sum(x*y)))

print("b = ----------------------------------------",end=" ")
print("= %.4f  " %b)
print("       ",n,"*  %.4f" %(sum(x**2)),"-   %.4f" %sum(x),"^2\n\n")

print("----------------------------------------------------------------------------------------------")
print("y = ax + b----> y = ",a,"* x","+",b)
print("----------------------------------------------------------------------------------------------")

