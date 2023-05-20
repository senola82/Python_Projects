import math
e = math.e
pi = math.pi

print("f(xz)*f(x2)<0 ifadesini kontrol et")
print("ÖNCE KÖKÜN VARLIĞINI KONTROL ET")

def newton_raphson(f, df, x, TOL):
    error = 1
    iterations = 0
    print("n", "     Xi", "         Xi+1", "         f(x)", "          f'(x)")
    while error > TOL:
        
        new_x = x - f(x)/df(x)
        print(iterations,"%.7f     " %x, "%.7f  "%new_x, "%.7f     " %f(x),"%.7f     " %df(x))
        error = abs(new_x - x)
        x = new_x
        iterations += 1
        
       
    print(f"Newton's Estimate = {x:.15f}\nIterations: {iterations}")

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
    print(f"Fibonacci's Estimate = {total:.15f}")

if __name__ == '__main__':
    f = lambda x: (x**3)-7*(x**2)+(14*x)-6#POLİNOM
    df = lambda x: (3*x**2)-(14*x)+14 #TÜREV
   
    newton_raphson(f, df, 0, 1e-6)#]f fonksiyon df fonksiyorun türevi. ARALIK VERİLİRSE TEK TEK DENE - 0 İ DEĞERİ
   
  #  f = lambda x: x**4 - 2*x**3 - 12*x*x + 16*x - 40
  #  df = lambda x: 4*x**3 - 6*x*x - 24*x + 16
 #   ddf = lambda x: 12*x*x - 12*x - 24
 #   newton_raphson(f, df, 1, 1e-5)
  #  modified_newton(f, df, ddf, 1, 1e-5)