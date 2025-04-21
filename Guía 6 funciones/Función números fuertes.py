# Escriba una función cuyo resultado sea un booleano que indique si el número dado
# como argumento es un número fuerte o no. Un número fuerte es aquel que es igual
# a la suma de los factoriales de sus dígitos. Por ejemplo,
# 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145
# Resuelva este problema utilizando el módulo math.

import math as mth

n = input("Ingrese un número entero positivo: ", )


def numero_fuerte(n):
    lista = list(n)
    largo = len(lista)
    entero = []

    j = 0
    while j < largo:
        entero.append(int(lista[j]))
        j = j + 1
    
    factor = 0
    i = 0

    while i < len(entero):
        factor = factor + mth.factorial(entero[i])
        i = i + 1                           
    if factor == int(n):                            
        return True
    else:
        return False
        
    
x = numero_fuerte(n)

print(x)  

    
