dinero = int(input("Ingrese una cantidad de dinero positiva: ", ))
# dinero = 205250
resto_de_billetes = dinero // 20000
dinero_resultante = dinero % 20000
# print(dinero_resultante)
resto_de_billetes_2 = dinero_resultante // 10000
dinero_resultante = dinero % 10000
# print(dinero_resultante)
resto_de_billetes_3 = dinero_resultante // 5000
dinero_resultante = dinero % 5000
# print(dinero_resultante)
# resto_de_billetes_4 = dinero_resultante // 2000
# dinero_resultante = dinero % 2000
# print(dinero_resultante)
resto_de_billetes_5 = dinero_resultante // 1000
dinero_resultante = dinero % 1000
# print(dinero_resultante)
resto_de_moneda = dinero_resultante // 500
dinero_resultante = dinero % 500
# print(dinero_resultante)
resto_de_moneda_2 = dinero_resultante // 100
dinero_resultante = dinero % 100
# print(dinero_resultante)
resto_de_moneda_3 = dinero_resultante // 50
dinero_resultante = dinero % 50
# print(dinero_resultante)
resto_de_moneda_4 = dinero_resultante // 10
dinero_resultante = dinero % 10
# print(dinero_resultante)
resto_de_moneda_5 = dinero_resultante // 5
dinero_resultante = dinero % 5
# print(dinero_resultante)
resto_de_moneda_6 = dinero_resultante // 1

if dinero < 0:
    print("El dinero ingresado debe ser positivo")
else:
    print("Se necesitarán:")
    print(resto_de_billetes, "Billetes de 20.000")  
    print(resto_de_billetes_2, "Billetes de 10.000")
    print(resto_de_billetes_3, "Billetes de 5.000")
    # print(resto_de_billetes_4, "Billetes de 2.000")
    print(resto_de_billetes_5, "Billetes de 1.000")
    print(resto_de_moneda, "Monedas de 500")
    print(resto_de_moneda_2, "Monedas de 100")
    print(resto_de_moneda_3, "Monedas de 50")
    print(resto_de_moneda_4, "Monedas de 10")
    print(resto_de_moneda_5, "Monedas de 5")
    print(resto_de_moneda_6, "Monedas de 1")


# 10 billetes de 20.000
# 0 billetes de 10.000 
# 1 billetes de 5.000 
# 0 billetes de 2.000 
# 0 billetes de 1.000 
# 0 monedas de 500 
# 2 monedas de 100 
# 1 monedas de 50 
# 0 monedas de 10 
# 0 monedas de 5. 
# 0 monedas de 1. 

