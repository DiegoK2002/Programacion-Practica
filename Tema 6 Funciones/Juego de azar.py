# ▪Construya un programa en Python que simule el sorteo de
# un juego de azar como el LOTO o el KINO
# ▪Considere que existe en Python el módulo random y tiene
# las funciones:
# – randint(inicio, final): Obtiene un número
# pseudoaleatorio entre el inicio y el final dado
# – choice(iterable): Selecciona un elemento desde la
# colección iterable

import random as rnd
from random import randint

m = 0

while m == 0:
    n = input("Ingrese 3 numeros entre 1 y 5 con los que participará separados por comas: ")
    n = n.split(",")
    m = 1

    lista_ganador = []
    lista_jugador = []

    j = 0

    while j < len(n):
        lista_jugador.append(int(n[j]))
        j = j + 1

    i = 0

    while i < 3:
        lista_ganador.append(randint(1,5))
        i = i + 1
    
    
    if lista_jugador[0] == lista_ganador[0] and lista_jugador[1] == lista_ganador[1] and lista_jugador[2] == lista_ganador[2]:
        print("¡¡FELICIDADES!! Usted ha ganado ABSOLUTAMENTE NADA!!")
        m = 0
    else:
        print("Lo sentimos, usted no ha ganado, los números ganadores eran:") 
        print(lista_ganador) 
        m = 0


    