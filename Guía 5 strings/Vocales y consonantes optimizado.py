frase = (input("Ingrese un texto para determinar sus vocales y consonantes: ", ))
minus = frase.lower()

consonantes = 0
vocales = 0

cons = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
voca = ["a","e","i","o","u"]

largo = len(cons)
largo_2 = len(voca)

i = 0

while i < largo:
    cantidad = minus.count(cons[i])
    consonantes = consonantes + cantidad
    i = i + 1
    
j = 0 
   
while j < largo_2:  
    cantidad_2 = minus.count(voca[j])
    vocales = vocales + cantidad_2
    j = j + 1

print(f"El número de consonantes es: {consonantes}") 
print(f"El número de vocales es: {vocales}") 


