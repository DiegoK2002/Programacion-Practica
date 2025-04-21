def mongolo(x,y):
    suma_x = lista * lista
    suma_y = lista_2 * lista_2
    result = suma_x + suma_y
    return result

x = (input("Ingrese un x: ", ))
y = (input("Ingrese un y: ", ))


xd = x.split(",")
yd = y.split(",")

yes = len(xd)
si = len(xd)
yest = len(yd)
yesnt = len(yd)

i = 0

while i < yes and i < yesnt:
    lista = int(xd[i])
    lista_2 = int(yd[i])
    si = lista + 1
    yest = lista_2 + 1
    print(f"La x más 1 es {si}")
    print(f"La y más 1 es {yest}")
    result = mongolo(lista,lista_2)
    print(f"El resultado de la suma de cuadrados es: {result}")
    i = i + 1



