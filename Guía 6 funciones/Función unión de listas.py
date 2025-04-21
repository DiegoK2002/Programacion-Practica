# Cree una función que entregue la intersección entre dos listas y otra que entregue
# la unión entre ambas.

# ej: [1,2,3] y [3,4,5]
# union = [1,2,3,4,5]
# interseccion = [3]

n = input("Ingrese la primera lista: ")
m = input("Ingrese la segunda lista: ")

def union_listas(n,m):
    lista_1 = n.split(",")
    lista_2 = m.split(",")
    largo = len(lista_1)
    union = []
    i = 0
    while i < largo:
        union.append(int(lista_1[i]))
        union.append(int(lista_2[i]))
        i = i + 1
    largo_in = len(union)
    j = 0
    while j < largo_in:
        if union.count(union[j]) > 1:
            union.pop(union.index(union[j]))
            largo_in = largo_in - 1
        else:
            union.sort()
        j = j + 1
    k = 0    
    while k < largo_in:
        if union.count(union[k]) > 1:
            union.pop(union.index(union[k]))
            largo_in = largo_in - 1
        else:
            union.sort()   
        k = k + 1  
    g = 0    
    while g < largo_in:
        if union.count(union[g]) > 1:
            union.pop(union.index(union[g]))
            largo_in = largo_in - 1
        else:
            union.sort()   
        g = g + 1      
    return union  



x = union_listas(n,m)
print(f"La unión de las listas es {x}") 