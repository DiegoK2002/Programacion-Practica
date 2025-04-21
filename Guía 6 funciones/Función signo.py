# Construya la función signo(x), la que debe tomar como parámetro un número y
# retornar 1, si este es positivo, -1, si es negativo o 0, si es cero.


n = int(input("Ingrese un Número: ", ))

def signo(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    elif n == 0:
        return 0
    
p = signo(n)
print(p)    