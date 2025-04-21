# Construya una función que tome como parámetros una lista y un valor y entregue
# como resultado una copia de la lista donde se haya eliminado el valor.

n = input("ingrese una lista: ", )
m = input("ingrese el valor a eliminiar: ", )

def eliminar(n,m):
    g = n.split(",")
    n = n.split(",")
    m = list(m)
    largo = len(m)
    i = 0
    while i < largo:
        p = n.index(m[i]) 
        n.pop(p)
        i = i + 1
    print(g)
    return n

p = eliminar(n,m)
print(p)