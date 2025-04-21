 # Construya un programa que convierta valores de longitud/distancia entre una
# unidad y otra, por ejemplo, el programa solicita un valor de longitud, la unidad en
# la que está expresada y la unidad a la que se quiere convertir y el sistema realiza las
# conversiones. Considere para su solución que las unidades de distancia/longitud
# que debe considerar son:
# Metro.
# Kilómetro.
# Centímetro.
# Milímetro.
# Milla.
# Legua.
# Pulgada.
# Yarda.
# Año Luz.
# Además, considere que cada transformación debe ser realizada en una única función, 
# sin embargo, algunas podrían tomar parámetros opcionales. Por ejemplo, puede definir
# la función pulgada_a_m, cuyos parámetros sean la cantidad de pulgadas a transformar y 
# un parámetro opcional, que indique si se entrega el resultado
# en metros, kilómetros, milímetros o centímetros.

print("Las longitudes disponibles son: kilometro, centimetro, milimetro, milla, legua, pulgada, yarda y año luz")
print("Ej: 35, metro, yarda")
n = input("Indique una unidad a transformar, unidad actual, unidad a transformar: ", )
n = n.split(",")

m = "metro"
k = "kilometro"
c = "centimetro"
ml = "milimetro"
mll = "milla"
lg = "legua"
pg = "pulgada"
yr = "yarda"
al = "año luz"
li = "libra"
kg = "kilo"


def convertir_longitud(n):
    if n[1] == m and n[2] == k:
        x = float(n[0])
        n = x / 1000
        return n
    if n[1] == m and n[2] == ml:
        x = float(n[0])
        n = x * 1000
        return n
    if n[1] == m and n[2] == c:
        x = float(n[0])
        n = x * 100
        return n
    if n[1] == m and n[2] == mll:
        x = float(n[0])
        n = x / 1609
        return n
    if n[1] == m and n[2] == lg:
        x = float(n[0])
        n = x / 4828
        return n
    if n[1] == m and n[2] == pg:
        x = float(n[0])
        n = x * 39.37
        return n
    if n[1] == m and n[2] == yr:
        x = float(n[0])
        n = x * 1.094
        return n
    if n[1] == m and n[2] == al:
        x = float(n[0])
        n = x / 9.461e+15
        return n
    if n[1] == li and n[2] == kg:
        x = float(n[0])
        n = x / 2.205
        return n
    
xd = convertir_longitud(n)
print(xd)    
print("Recuerde que el punto(.) es el separador decimal")