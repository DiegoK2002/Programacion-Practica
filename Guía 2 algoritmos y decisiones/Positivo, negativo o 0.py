i = 0
while i == 0:
    numero = int(input("Ingrese un número: ", ))
    i = i + 1
    if numero > 0:
        print("El número ingresado es positivo")
        i = i - 1
    if numero < 0:
        print("El número ingresado es negativo") 
        i = i - 1
    if numero == 0:
        print("El número ingresado es no-negativo, es decir igual a 0")  
        i = i - 1