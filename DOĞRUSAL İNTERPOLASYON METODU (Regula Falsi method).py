2# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:09:53 2023

@author: senol
"""

# ARA DEĞER TEOREMİ polinom HESAPLAMASI 


print("f(xz)*f(x2)<0 ifadesini kontrol et")


print("ÖNCE KÖKÜN VARLIĞINI KONTROL ET")
#f(x1)*f(x2)<0 ise en az bir kökün varlığı söz konusudur.







import math

n=0
def polinomhesapla(x):
   return 1.5+5*x-2*(pow(x,3))-3*(pow(x,3/5))
   #return pow(x,3)-7*(pow(x,2))+14*x-6
   #return ((68.1*9.81)/x)*(1-pow(2.718281,-(x*10)/68.1))-40
    

polinomhesapla(2)

a=int(input("Birinci Sayıyı girin ="))
b=int(input("İkinci Sayıyı girin ="))
c=0
sayac=int(input("iterasyon(döngü Sayısı) girin ="))
#print("X1\t\t---X2\t\t--- X3   \t\t---f(x1)\t\t---f(x2)  \t\t--- f(x3)")
print("n", "     X1", "         X2", "         X3", "          f(X1)","       f(X2)", "        f(X3)")
while True:
    
  
    pa=polinomhesapla(a)
    pb=polinomhesapla(b)
    c=((b*pa)-(a*pb))/(pa-pb)   # 1. FORMÜL
   # c=b-((pb*(a-b))/(pa-pb))     # 2. FORMÜL
    pc=polinomhesapla(c)
    
    print(n+1, "%.7f   " % a, "%.7f   " % b, "%.7f   " % c, "%.7f   " % pa,"%.7f   " % pb,"%.7f   " % pc)
  #  print(" ",a,"\t\t---",b,"\t\t---",c,"\t\t---",pa,"\t\t---",pb,"\t\t---",pc)
   
    if pa*pc<0:
        b=c
    if pa*pc>0:
        a=c
    sayac-=1


 #  print("Sayac =", sayac,end=" - ")
 #  print("C POLİNOM değeri =",pc)

    if sayac==0:
        
        break