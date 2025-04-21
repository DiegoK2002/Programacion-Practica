#5! = 5*4*3*2*1

def factorial(n):
    if n < 998:
        if n == 0:
            return 1
        return n * factorial(n - 1)
    else:
        return print("El número es demasiado grande")

variable = 1

while variable > 0:
    n = int(input("Ingrese un número: ", )) 
    variable = variable - 1
    di = factorial(n)
    print(di)
    variable = variable + 1