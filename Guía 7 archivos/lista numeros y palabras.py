lista = [1,2,4,'hola','mundo']

lista_sep = []

lista_num = []
lista_text = []

lista_numcua = []
lista_lentext = []


letras = 'abcdefghijklmnñopqrstuvwxyz'
letras = list(letras)

ñ = str(lista)
ñ = ñ.strip('[')
ñ = ñ.strip(']')

caracter = ('[',']')

for caracter in ñ:
    if caracter.isdigit():
        lista_num.append(caracter)
    if caracter.isalpha():
        lista_text.append(ñ[ñ.index(caracter)])
        
        
# for carac in lista:
#     for caracter in ñ:
#         if caracter.isdigit():     
#             lista.pop(lista[lista.index(carac)])
    # if carac.isalpha():
    #     lista_text.append(carac)

# for carac in lista_num:
#     carac = int(carac)
#     carac = carac ** 2
#     lista_numcua.append(carac)
    
# for cac in lista_text:
#     for letra in letras:
#         if cac != letras:
#             # posicion = lista_text.index(cac)
#             # pos = lista_text[posicion]
#             lista_text.pop(cac)   