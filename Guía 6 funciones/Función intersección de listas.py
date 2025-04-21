# Cree una función que entregue la intersección entre dos listas y otra que entregue
# la unión entre ambas.

# ej: [1,2,3] y [3,4,5]
# union = [1,2,3,4,5]
# interseccion = [3]

n = input("Ingrese la primera lista: ")
m = input("Ingrese la segunda lista: ")

def interseccion_listas(n,m):
    lista_1 = n.split(",")
    lista_2 = m.split(",")
    largo = len(lista_1)
    inter = []
    i = 0
    while i < largo:
        inter.append(int(lista_1[i]))
        inter.append(int(lista_2[i]))
        i = i + 1  
    largo_in = len(inter)
    j = 0
    while j < largo_in:
        if inter.count(inter[j]) == 1:
            inter.pop(inter.index(inter[j]))
            largo_in = len(inter)
        else:
            inter.sort()
        j = j + 1   
    g = 0
    while g < largo_in:
        if inter.count(inter[g]) == 1:
            inter.pop(inter.index(inter[g]))
            largo_in = len(inter)
        else:
            inter.sort()
        g = g + 1 
    s = 0
    while s < largo_in:
        if inter.count(inter[s]) == 1:
            inter.pop(inter.index(inter[s]))
            largo_in = len(inter)
        else:
            inter.sort()
        s = s + 1     
    k = 0    
    while k < largo_in:
        if inter.count(inter[k]) > 1:
            inter.pop(inter.index(inter[k]))
            largo_in = largo_in - 1
        else:
            inter.sort()   
        k = k + 1 
    d = 0    
    while d < largo_in:
        if inter.count(inter[d]) > 1:
            inter.pop(inter.index(inter[d]))
            largo_in = largo_in - 1
        else:
            inter.sort()   
        d = d + 1      
    return inter

x = interseccion_listas(n,m)
print(f"La intersección de las listas es {x}")  

