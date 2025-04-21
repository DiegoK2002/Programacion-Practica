# Construya un programa en Python que reciba como entrada una cantidad n de filas 
# y una cantidad m de columnas y entregue como resultado un archivo con una matriz 
# con números aleatorios de dichas dimensiones, el archivo de salida debe llamarse 
# ‘matriz.txt’ y cada celda debe contener un número aleatorio entre -n * m y n * m.

import random as rn

n = int(input('Ingrese una cantidad de filas: '))
m = int(input('Ingrese una cantidad de columnas: '))

archivo = open('matriz.txt','w')

matriz = []

j = 0
k = 0
h = 0


while j < n:
    while h < n:
        while k < m:
            matriz.append(rn.randint(-n*m,n*m))
            k = k + 1
        archivo.write('\n'+str(matriz)) 
        matriz = []
        k = 0
        h = h + 1
    j = j + 1
        
        
    

    
archivo.close()