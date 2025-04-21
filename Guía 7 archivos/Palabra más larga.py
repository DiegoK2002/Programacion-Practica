# Construya un programa que encuentre la palabra más larga en un texto, 
# considere que el texto le será entregado desde un archivo llamado ‘texto.txt’. 
# Use como base el ejercicio para una sola línea visto en clases.

archivo = open('texto.txt','r')

texto = ''

letras = 'abcdefghijklmnñopqrstuvwxyz'
letras = list(letras)

cont= []

for linea in archivo:
    texto = texto + linea
    
texto = texto.lower()

caracter = ','

for x in range(len(texto)):
    texto = texto.replace(caracter[x],' ')
    break
    
    
    
texto_2 = texto.split(' ')

i = 0
j = 0
h = 0

            
while i < len(texto_2):
    while j < len(letras):
        if texto_2[i].count(letras[j]) == 0:
            j = j + 1
        else:
            m = texto_2[i].count(letras[j])
            h = h + m  
            j = j + 1
    cont.append(h)
    i = i + 1
    j = 0
    h = 0    
    
maxi = [0]    
    
z = 0

while z < len(cont):
    if cont[z] > maxi[0]:
        maxi[0] = cont[z]
    z = z + 1
    
palabramax = []

palabramax.append(texto_2[cont.index(maxi[0])])    



print(f'La palabra más larga del texto es: {palabramax} con {maxi[0]} letras')
    
    
archivo.close()    