texto = 'hola mundo'
texto = texto.split()
# texto = texto.pop(texto[texto.index(" ")])

letras = 'abcdefghijklmnñopqrstuvwxyz'
letras = list(letras)

cont= []

h = 0
i = 0
j = 0
            
            
while i < len(texto):
    while j < len(letras):
        if texto[i].count(letras[j]) == 0:
            j = j + 1
        else:
            m = texto[i].count(letras[j])
            h = h + m  
            j = j + 1
    cont.append(h)
    i = i + 1
    j = 0
    h = 0           
            
    

