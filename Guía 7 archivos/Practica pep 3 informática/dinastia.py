def rom(num):
    val =[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syb =["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

archivo = open('dinastia.txt','r')
texto = ''
    
for caracter in archivo:
    texto = texto + caracter

nombre = texto.split('\n')

nomrom = []

i = 1

for carac in nombre:
    if nombre.count(carac) > 1:
        carac = carac + ' ' + rom(i)
        nomrom.append(carac)
        i = i + 1
    else:
        carac = carac + rom(1)
        nomrom.append(carac)



archivo.close()