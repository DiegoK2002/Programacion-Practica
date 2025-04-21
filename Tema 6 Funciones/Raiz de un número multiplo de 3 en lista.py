# ▪ Construya un programa en Python que imprima por pantalla la raíz
# cuadrada de los números múltiplos de 3 de la siguiente lista de
# valores

import math as mt
from math import isqrt

lista = [10,33,9,14,18,14,12,21,50,55,60]
lista_sqrt = []

i = 0

while i < len(lista):
    if lista[i] % 3 == 0:
        lista_sqrt.append(mt.isqrt(lista[i]))
    else:
        lista_sqrt.append(lista[i])
    i = i + 1
    
print(lista)    
print(lista_sqrt)    
