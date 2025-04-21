# Construya una función que, a partir de dos puntos representados como listas de
# la forma [x, y], retorne como resultado la distancia entre estos puntos. Si el
# programador no ingresa el segundo punto, la función debe asumir que este es el
# punto (0, 0) (representado por la lista [0, 0]).

from math import isqrt


coordenada = [] 
llegada = []


p = input("Ingrese las coordenadas x,y en las que está actualmente: ")
q = input("Ingrese las coordenadas w,z a las que quiere llegar: ")

coordenada = p.split(",")
llegada = q.split(",")

x = int(coordenada[0])
y = int(coordenada[1])

if q == "":
    w = 0
    z = 0
else:    
    w = int(llegada[0])
    z = int(llegada[1])


def distancia(x,y,w,z):
    distance = isqrt((w-x)**2 + (z-y)**2)
    return distance          


x = distancia(x,y,w,z)
print("La distancia entre ambos puntos es", x)
