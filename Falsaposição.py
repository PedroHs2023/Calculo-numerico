#importar a biblioteca de matematica
import math
import numpy as np

# Definir um intervalo [a,b] e erro
a =  -4
b =  -3
e = 0.001

#Definir uma funcao
def f(x):
    return x*x*x - 9*x+3


#Teorema de Bolzano
if f(a)*f(b) < 0:
    while True:

        xi = (a*f(b) - b*f(a))/ (f(b) - f(a))
        fxi = round(xi,4)

        fx = f(xi)
        fx = round(fx,4)

        Rb = round(b,4)
        
        print("Valores: a =", a, "b =", Rb, "x_ns =", fxi, "Erro =", fx)
        if math.fabs(fx) < e:
            print("Solucao : ", "f(x) =", fx, "x =", fxi)
            break
        if f(xi) == 0:
            print("A raiz e:", xi)
            break
        else: 
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi               
        
   


else:
    print("Nao tem raizes!")