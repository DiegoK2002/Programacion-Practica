texto = (input("Ingrese un texto para determinar sus vocales y consonantes: ", ))
minu = texto.lower()

vocales = 0
consonantes = 0

lista = list(minu)
# print(lista)

if minu.count("a") > 0:
    vocales = vocales + minu.count("a")
if minu.count("e") > 0:
    vocales = vocales + minu.count("e")    
if minu.count("i") > 0:
    vocales = vocales + minu.count("i")
if minu.count("o") > 0:
    vocales = vocales + minu.count("o")
if minu.count("u") > 0:
    vocales = vocales + minu.count("u")
print("El número de vocales es: ", vocales)    

if minu.count("b") > 0:
    consonantes = consonantes + minu.count("b")
if minu.count("c") > 0:
    consonantes = consonantes + minu.count("c")    
if minu.count("d") > 0:
    consonantes = consonantes + minu.count("d")
if minu.count("f") > 0:
    consonantes = consonantes + minu.count("f")
if minu.count("g") > 0:
    consonantes = consonantes + minu.count("g")
if minu.count("h") > 0:
    consonantes = consonantes + minu.count("h")
if minu.count("j") > 0:
    consonantes = consonantes + minu.count("j")    
if minu.count("k") > 0:
    consonantes = consonantes + minu.count("k")
if minu.count("l") > 0:
    consonantes = consonantes + minu.count("l")
if minu.count("m") > 0:
    consonantes = consonantes + minu.count("m")
if minu.count("n") > 0:
    consonantes = consonantes + minu.count("n")
if minu.count("p") > 0:
    consonantes = consonantes + minu.count("p")    
if minu.count("q") > 0:
    consonantes = consonantes + minu.count("q")
if minu.count("r") > 0:
    consonantes = consonantes + minu.count("r")
if minu.count("s") > 0:
    consonantes = consonantes + minu.count("s")
if minu.count("t") > 0:
    consonantes = consonantes + minu.count("t")
if minu.count("v") > 0:
    consonantes = consonantes + minu.count("v")    
if minu.count("w") > 0:
    consonantes = consonantes + minu.count("w")
if minu.count("x") > 0:
    consonantes = consonantes + minu.count("x")
if minu.count("y") > 0:
    consonantes = consonantes + minu.count("y")   
if minu.count("z") > 0:
    consonantes = consonantes + minu.count("z")     

print("El número de consonantes es: ", consonantes)
    