#importar a biblioteca de matematica
import math
import numpy as np

# Definir um intervalo [a,b] e erro
a =  1
b =  2
e = 0.01

#Definir uma funcao
def f(x):
    return x*x - 3


#Teorema de Bolzano
if f(a)*f(b) < 0:
    while ( math.fabs(b-a)/2 > e):
        xi = (a+b)/2
        print("valores : ", a, b, (a+b)/2,math.fabs(b-a)/2)
        if f(xi) == 0:
            print("A raiz e:", xi)
            break
        else: 
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi               
        
    print("valores : ", a, b, (a+b)/2,math.fabs(b-a)/2)


else:
    print("Nao tem raizes!")

