# Construya un programa en Python que cuente la cantidad de vocales y consonantes en un texto
# en inglés entregado en un archivo de entrada llamado ‘texto.txt’

# conso = 164

vocals = 'aeiou'
vocals_list = list(vocals)

conso = 'bcdfghjklmnñpqrstvwxyz'
cons_list = list(conso)

con = []
voc = []

def leer_archivo(nombre):
    nombre = nombre + ".txt"
    with open(nombre, 'r') as archivo:
        texto = ''
        for linea in archivo:
            texto = texto + linea
    return texto
        
        
archivo = leer_archivo('texto')        
        
def contar_consonantes(texto):
    contador = 0
    vocales = "aeiouáéíóúü"
    for caracter in texto:
        if caracter.isalpha() and not\
            (caracter.lower() in vocales):
                contador += 1
    return contador     

ñ = contar_consonantes(archivo)