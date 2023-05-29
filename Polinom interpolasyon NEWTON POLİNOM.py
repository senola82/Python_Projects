# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 21:58:43 2023

@author: senol.a82@hotmail.com
"""

# İKİ BİLİNMEYENLİ NEWTON POLİNOMlARI HESAPLAMASI

import math
e=math.e
pi=math.pi
log=math.log

#x0 = a  x1=b

def f(x):    
    sonuc=float(log(x))        # POLİNOM FONKSİYON BURAYA YAZILACAK
   # sonuc=float(e**x)
    return sonuc


def newton_polinom(x0,x1,x):    
    dlty=f(x1)-f(x0)            #dlty=y=f(x)= f(b)-f(a) 
    h=  x1 - x0                 # h= b-a
    sonuc=f(x0)+((dlty/h)*(x-x0))        
    return sonuc



#-------------------------------- VERİLER   BURAYA YAZILACAK
x0 = 0.20           #a 
x1 = 0.30           #b
x=   0.26         #istenen değer  


print("""

-------
h=b-a
#deltY= f(b)-f(a) 
                              FORMÜL                               
------------------------------------------------------------------------
|              f(b)-f(a)                          f(x1)-f(x0)          |
| y = f(a) +   --------- * (x-a)   veya   f(x0)+  ---------- *(x -x0)  |
|               b - a                              x1 - x0             |
------------------------------------------------------------------------

""")
                    
print("\n-------------------------------FORMÜLDE YERİNE YAZMA---------------------------------------")

print("               (%.4f" % f(x1),") - (%.4f" % f(x0),")                              %.4f" %float(f(x1)-f(x0)))
print("y = %.4f"% f(x0),"+  ------------------------ *(%.2f" %x, "- %.2f" % x0,")=%.4f"% f(x0), "+ ----------- * (%.2f" %(x-x0),")= %.4f" % newton_polinom(x0,x1,x))
print("                   %.4f"% x1, "-"," %.4f"% x0,"                                 %.4f"%float(x1-x0))


print("-------------------------------------------------------------------------------------------")
