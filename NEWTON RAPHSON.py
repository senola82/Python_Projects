import math
e = math.e
pi = math.pi

f = lambda x: (e**-x)-x#POLİNOM
df = lambda x: (-e**-x)-1 #TÜREV

X0=0 # BAŞLANGIÇ DEĞERİ

print("""
           ÖNCE TEMEL FORMÜLÜ KULLANABİLMEK İÇİN FONKSİYONUN X E GÖRE TÜREVİ ALINIR 
       
                -------------------FORMÜL-------------------
         
                                      f(Xi)
                        Xi+1 = Xi - ----------
                                      f'(Xi) 
                --------------------------------------------     
                 X0 = 0 BAŞLANGIÇ DEĞERİ İSE
                 
                 fonksiyonumuz f(x) = e**-x -x olsun.  Türevi : f'(x) = -e**-x-1 olur.
                 
                 buradan  
                 f(0)= e**-0-0 = 1       f'(0)=-e**-0-1 = -2
                 
                           e**-x -x          1
                 X1 = X0 - --------- = 0 - ----- = 0,5  
                           -e**-x-1         -2
                           
               X1 İN DEĞERİ 0,5 OLUR SONRA BU DEĞER İLE İŞLEMLER TEKRARLANIR.               
        
       """)




def newton_raphson(f, df, x, TOL):
    error = 1
    iterations = 0
    print("         f(0)         ", f(x)                                                         )
    print("X1 = 0 - ----- = ",x, "- ----- = ", x - f(x)/df(x)                                    )
    print("        f'(0)        ",df(x)                                                          )
    
    print("n", "     Xi", "         Xi+1", "         f(x)", "          f'(x)")
    while error > TOL:
        
        new_x = x - f(x)/df(x)
        print(iterations,"%.7f     " %x, "%.7f  "%new_x, "%.7f     " %f(x),"%.7f     " %df(x))
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        
       
    print(f"\nNewton's Estimate = {x:7f}\nIterations: {iterations}")

def modified_newton(f, df, ddf, x, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        f_x = f(x)
        d_x = df(x)
        new_x = x - (f_x*d_x)/(d_x*d_x - f_x*ddf(x))
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        print(f'x{iterations}: {x}')
    print(f"Modified Newton Estimate = {x:.15f}\nIterations: {iterations}")

def fibonacci_estimate():
    values = [1, 22, 7, 42, 33, 4, 40]
    total = 0
    for i in range(len(values)):
        total += values[i]/(60**i)
    print(f"Fibonacci's Estimate = {total:.7f}")

if __name__ == '__main__':     
   
    newton_raphson(f, df, X0, 1e-6)#]f fonksiyon df fonksiyorun türevi. ARALIK VERİLİRSE TEK TEK DENE - 0 İ DEĞERİ
   
  #  f = lambda x: x**4 - 2*x**3 - 12*x*x + 16*x - 40
  #  df = lambda x: 4*x**3 - 6*x*x - 24*x + 16
 #   ddf = lambda x: 12*x*x - 12*x - 24
 #   newton_raphson(f, df, 1, 1e-5)
  #  modified_newton(f, df, ddf, 1, 1e-5)