variable = 1
while variable > 0:
    n = int(input(" Ingrese un número natural: ",))
    variable = variable - 1
    if n > 0:
        suma = int((n * (n+1))/2)
        print("La suma de los primeros", n,"números es: ", suma);
        variable = variable + 1  
    else:
        print("El número ingresado no es parte del conjunto de los naturales");        
        variable = variable + 114
    