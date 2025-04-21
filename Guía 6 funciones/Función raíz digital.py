# Construya una función que obtenga la raíz digital de un número entero. Esta es
# un número de 0 a 9 que se obtiene al sumar todos los dígitos del número. Si
# el resultado es mayor a 10, se repite la suma sobre este nuevo resultado hasta
# obtener un número entre 0 y 9, ambos inclusive.

n = input("Ingrese un número entero: ", )

def raiz_digital(n):
    suma = 0
    summa = 0
    summma = 0
    i = 0
    j = 0
    k = 0
    lista = list(n)
    largo = len(lista)
    while i < largo:
        suma = suma + int(lista[i])
        i = i + 1
    h = str(suma)    
    summ = list(h) 
    largo_2 = len(summ)
    while j < largo_2:
        summa = summa + int(summ[j])
        j = j + 1
    g = str(summa)    
    summm = list(g) 
    largo_3 = len(summm)   
    while k < largo_3:
        summma = summma + int(summm[k])
        k = k + 1
    return summma    
        
x = raiz_digital(n)
print(f"La raiz digital de {n} es {x}")

