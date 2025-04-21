# Construya un programa en Python que cuente la cantidad de vocales y consonantes en un texto
# en inglés entregado en un archivo de entrada llamado ‘texto.txt’

archivo = open('texto.txt','r')

texto = ''

cons = 'bcdfghjklmnñpqrstvwxyz'
vocs = 'aeiou'

cons = list(cons)
vocs = list(vocs)

consonantes = 0
vocales = 0

for linea in archivo:
    texto = texto + linea
    
minus = texto.lower()    

i = 0

while i < len(cons):
    ñ = minus.count(cons[i])
    consonantes = consonantes + ñ
    i = i + 1
    
j = 0
    
while j < len(vocs):
    h = minus.count(vocs[j])
    vocales = vocales + h
    j = j + 1
    
print(f'el número de consonantes en el archivo es de: {consonantes}')    
print(f'el número de vocales en el archivo es de: {vocales}')    

archivo.close()