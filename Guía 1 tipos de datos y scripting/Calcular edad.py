nacimiento = input("Ingrese su anio de nacimiento: ", )
nacimiento_a = int(nacimiento)
anio = 2022
if nacimiento_a > 0:
    anio = anio - nacimiento_a
    print("Su edad actual es: ", anio)
else: 
    print("Ingrese un anio valido")