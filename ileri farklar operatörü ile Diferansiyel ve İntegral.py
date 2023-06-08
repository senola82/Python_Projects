# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:55:34 2023

@author: senol.a82@hotmail.com
"""
import math
e=math.e
pi=math.pi
log=math.log


#---------------------------------------------------------------------- DEĞERLERİ YERİNE YAZ

def f(x):
    #return (e**x) + 1 # fonksiyon
    return (x**2) + 1 
    #♠return 2*(x**2)+(3*x)-2 

x0, h = 1.3, 0.2   # h ve x0 değerlerini düzelt


#--------------------------------------------------------------------------------

hfark=x0
liste=[[],[],[],[],[],[],[],[]]

derece = float(input("kaçıncı dereceden ileri sonlu olsun: "))

y=float(input("istenen fonksiyonu giriniz : "))  # türevi istenen nokta  yazılacak. tablodaki x e karşılık len değerin 1 eksiği yani 1 isteniyorsa x 1 den başlıyorsa Y=0 ALINACAK

if x0==1.0:
    y=y-1

if (derece == 0.0): 
    print(f(h))
    exit(1)

baslangic = derece + 1.0 

baslangic2=derece
a=[]
for i in range(0,int(baslangic)):
    a.append(float(i))
    
b=[]
for i in range(0,int(baslangic2)):
    b.append(float(i))
    
    
    

for i in a: 
    liste[0].append(f(x0))
    x0 += h


# LİSTE VERİLİRSE BURAYA GİR (FONKSİYON VERİLMEZSE )

liste[0]=[-4.8479,-4.4375,-3.5839,-2.0759,0.3361,3.9401,9.0625]
#liste[0]=[3.718,8.389,21.086,55.598]



    




#İLERİ FARK OPERATÖRÜ İÇİN bunu aktif et   
for ii in b:     
    for i in range(0, len(liste[int(ii)])-1):             
                liste[int(ii)+1].append((liste[int(ii)][i+1] - liste[int(ii)][i]))        
         
"""
#GERİ  FARK OPERATÖRÜ İÇİN  bunu aktif et
for ii in b:
    for i in range(0, len(liste[int(ii)])-1):
        liste[int(ii)+1].append((liste[int(ii)][i] - liste[int(ii)][i+1])) 
        
""" 
for i in range(0, len(liste[0])):   
    while True:
        if len(liste[int(i)+1])!=len(liste[0]):
            liste[int(i)+1].append(0.0)
        else:
            break


    
hlist=[]
             
print("\n-------------------------------FARK TABLOSU-------------------------------------------------\n")

j=0
j2=0
print(" x    -      f   -      df   -     d^2f   -   d^3f  -    d^4f    -     d^5f    -  d^6f  ")

for ii in range(0,len(liste[0])): #İLERİ FARK bunu aktif et
    print(hfark,end=" ")
    hlist.append(hfark)
    for i in range(0, len(liste[int(ii)])+1):       
        if (liste[j][j2])!="":
            print("     %.4f"%(liste[j][j2]),end=" ")
            j+=1
        elif (liste[j][j2])=="":
            liste[j][j2]=0.0
            
    j2+=1
    j=0
    hfark+=h
    print("\n")


print("""
-------------------------------------------------------------------------
                            TÜREV FORMÜLÜ                               
-------------------------------------------------------------------------
|      1            delta^2   delta^3   delta^4   delta^5    ....       |
| D = --- *(delta - ------- + ------- - ------- + ------- - ---- )*f(x) |
|      h              2          3         4        5        ...        |
-------------------------------------------------------------------------
""")

print("\n---------------TÜREV FORMÜLÜNDE YERİNE YAZMA -------------------------------------")

print("         1               %.4f"%liste[2][int(y)],"   %.4f"%liste[3][int(y)],"  %.4f"%liste[4][int(y)],"   %.4f"%liste[5][int(y)] )   
print("Df(x) = -- * (%.4f"%liste[1][int(y)],"-  -------- + ------- - ------- + -------- )" )
print("       ",h, "                2          3         4         5    ")   
      
print("f'(",y,")=%.4f"%((1/h)*((liste[1][int(y)]/1) - (liste[2][int(y)]/2) + (liste[3][int(y)]/3) - (liste[4][int(y)]/4)+(liste[5][int(y)]/5))))
    
print("""
------------------------------------------------------------------------------------
                            
                              İNTEGRAL  FORMÜLÜ                                            
-----------------------------------------------------------------------------------------
|                                  delta    delta^2   delta^3   delta^4     ....        |
| int xiden xi+h f(x)dx =  h *(1 + ------- - ------ + ------- - ------- + -------)*f(x) |
|                                    2        12       24         720       ....        |
-----------------------------------------------------------------------------------------
""")


print("\n---------------İNTEGRAL FORMÜLÜNDE YERİNE YAZMA -------------------------------------")

print("                                         %.4f"%liste[1][int(y)],"    %.4f"%liste[2][int(y)],"   %.4f"%liste[3][int(y)] ,"    %.4f"%liste[4][int(y)] )   
print("int xiden xi+h f(x)dx =" ,h, " * (%.4f"%liste[0][int(y)],"+  -------- - ------- + ------- - -------- )" )
print("                                            2          12         24         720    ")   
print("-------------------------------------")      
print("f(",y,")=%.4f"%((h)*((liste[0][int(y)]/1) + (liste[1][int(y)]/2) - (liste[2][int(y)]/12) + (liste[3][int(y)]/24) - (liste[4][int(y)]/720) )),"Numerik değeri bulunur.|")#-(liste[4][int(y)]/720))))
print("-------------------------------------")
print("\n Analitik değeri için Fonksiyonun Türevi alınarak hesaplanır ve Numerik ile analitik değer arasındaki fark bize hata payını verir.")
print("""
      
      x^2+1 in integral hesabı için türevi ; x üssü bir arttırılır ve yeni üs değerine bölünür.
      1 in türevi yanında gizli bir x olduğunu gösterir
      
                         x^3 
    x^2+1  TÜREV =      ----- + x
                          3
           
""")

print("Analitik çözüm.",end=" ")

print(" = %.4f"%float(((h**3)/3)+h))

print("-----------------------------------------------------------------------------------------")