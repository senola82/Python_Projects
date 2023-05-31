# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:51:59 2023

@author: senol
"""



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
   # return cos(x)+sin(1+x**2)-1
    return (e**-x)-x
print("""
      
ÖNCE TEMEL FORMÜLÜ KULLANABİLMEK İÇİN FONKSİYONUN X E GÖRE TÜREVİ ALINIR 

     -------------------FORMÜL-------------------

                           f(Xi)*(Xi-1 - Xi)
             Xi+1 = Xi - --------------------
                           f(Xi-1) - f(Xi) 
     --------------------------------------------     
     
     xi-1 = X-1 = 0.0    ve     xi = X0 = 1.0 BAŞLANGIÇ DEĞERİ İSE
     
     fonksiyonumuz f(x) = e**-x -x olsun.  
     
     buradan  
     f(xi)= f(x0)= e**-1-1 = 1/e - 1     f(xi-1)= f(x-1)=-e**-0 = 1
     
                       (-0,63212055)*(0 - 1)
     Xi+1 = x1 = 1 -  ---------------------- = 0,61270
                        1 - (-0,63212055)
     """)

print("\nn", "      Xi-1", "           Xi", "          Xi+1", "         f(xi-1)", "          f(xi)")
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
 


print("\niterasyon:",secant(0,1,pow(10,-6),100))#x-1 , x0,



