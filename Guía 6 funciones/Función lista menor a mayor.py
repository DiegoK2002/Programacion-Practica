# Construya una función que retorne si una lista de números entregada como argumento
# está ordenada de menor a mayor.

#SOLO SE PUEDE DEL 0 AL 99

n = input("Ingrese una lista de menor a mayor: ", )

x = []

def orden_lista(n):
    lista = n.split(",")
    lista_2 = n.split(",")
    lista_2.sort(reverse = False)
    largo = len(lista)
    veracidad = []
    veracid = 0
    i = 0
    g = 0
    while g < largo:
        lista[g] = int(lista[g])
        g = g + 1
    k = 0
    while k < largo:
        lista_2[k] = int(lista_2[k])
        k = k + 1
    while i < largo:
        if lista[i] == lista_2[i]:
            veracidad.append(True)
        else:
            veracidad.append(False)
        i = i + 1
    largo_v = len(veracidad)    
    j = 0
    while j < largo_v:
        veracid = veracid + veracidad[j]
        if veracid == largo:
            x = True
        else:
            x = False
        j = j + 1        
    return x             

p = orden_lista(n)
print(p)