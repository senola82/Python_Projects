# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:51:59 2023

@author: senol
"""


print("f(xz)*f(x2)<0 ifadesini kontrol et")
print("ÖNCE KÖKÜN VARLIĞINI KONTROL ET")

import math
e = math.e
sin=math.sin
pi = math.pi
cos=math.cos
# globals
APPROX = 0.1
TOL = 10**-5
N = 100

# function we are using
def f(x):
    #return (e**x/x)-(sin(x)/x**2)+(2*x)-10#POLİNOM
    return cos(x)+sin(1+x**2)-1

print("n", "        Xi-1", "           Xi", "           Xi+1", "         f(i-1)", "        f(i)")
# Actual Secant Method
def secant(p0, p1, tol, N):
    for i in range(0, N):
        p = p1 - ((f(p1)*(p0-p1))/(f(p0) - f(p1)))
        if abs(p-p1) < tol:
            return i
        print (i,"   %.7f     " %p0,"%.7f     " %p1,"%.7f     " %p,"%.7f     " %f(p0),"%.7f     " %f(p1))
        
        p0 = p1
        p1 = p
        
    return "Them method failed after {} iterations">format(N)        
 


print("iterasyon:",secant(0,3,pow(10,-6),100))#x-1 , x0,



