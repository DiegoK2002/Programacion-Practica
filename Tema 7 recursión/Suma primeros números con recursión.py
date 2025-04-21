n = int(input("Ingrese un número: ", )) 

def suma(n):
    if n == 0:
        return 0
    return n + suma(n-1)
    
di = suma(n)
print(di)   
 