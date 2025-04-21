presupuesto = int(input("Ingrese su presupuesto para comprar pelotas y camisetas: ", ))
# presupuesto = 60000
pelotas = [5000,8000,12000]
camisetas = [40000,50000,60000]

gastar = 0
comprar = 0

#menos a 5000
if presupuesto < 5000:
    gastar = 0
    comprar = 1
    print("Se va a gastar: ", gastar, "$ no alcanza el presupuesto")
    
#5000 a 7999    
if presupuesto < 8000 and comprar == 0:
    gastar = 5000
    comprar = 2
    print("Se va a gastar: ", gastar, "$ en la pelota de 5000") 
    
# #8000 a 11999    
if presupuesto < 12000 and comprar == 0:
    gastar = 8000
    comprar = 3
    print("Se va a gastar: ", gastar, "$ en la pelota de 8000")   
    
# #de 12000 a 39999   
if presupuesto < 40000 and comprar == 0:
    gastar = 12000
    comprar = 4
    print("Se va a gastar: ", gastar, "$ en la pelota de 12000")
    
#de 40000 a 44999
if presupuesto >= 40000 and presupuesto < camisetas[0] + pelotas[0] and comprar == 0:
    gastar = 40000
    comprar = 5
    print("Se va a gastar: ", gastar, "$ en la camiseta de 40000") 
    
#de 45000 a 47999    
if presupuesto >= camisetas[0] + pelotas[0] and presupuesto < camisetas[0] + pelotas[1]  and comprar == 0:
    gastar = pelotas[0] + camisetas[0]
    comprar = 6
    print("Se va a gastar: ", gastar, "$ en la camiseta de 40000 + la pelota de 5000") 

#de 48000 a 49999
if presupuesto >= camisetas[0] + pelotas[1] and presupuesto < camisetas[1] and comprar == 0:
    gastar = pelotas[1] + camisetas[0]
    comprar = 7
    print("Se va a gastar: ", gastar, "$ en la camiseta de 40000 + la pelota de 8000")
    
#de 50000 a 51999
if presupuesto >= camisetas[1] and presupuesto < camisetas[0] + pelotas[2] and comprar == 0:
    gastar = 50000
    comprar = 8
    print("Se va a gastar: ", gastar, "$ en la camiseta de 50000") 
    
#de 52000 a 54999
if presupuesto >= 52000 and presupuesto < camisetas[1] + pelotas[0] and comprar == 0:
    gastar = 52000
    comprar = 8
    print("Se va a gastar: ", gastar, "$ en la camiseta de 40000 + la pelota de 12000")     
    
#de 55000 a 57999
if presupuesto >= 55000  and presupuesto < camisetas[1] + pelotas[1] and comprar == 0:
    gastar = 55000
    comprar = 9
    print("Se va a gastar: ", gastar, "$ en la camiseta de 50000 + la pelota de 5000")     
    
#de 58000 a 59999
if presupuesto >= 58000  and presupuesto < camisetas[2] and comprar == 0:
    gastar = 58000
    comprar = 10
    print("Se va a gastar: ", gastar, "$ en la camiseta de 50000 + la pelota de 8000")     
            
#de 60000 a 61999
if presupuesto >= 58000 and presupuesto < camisetas[1] + pelotas[2] and comprar == 0:
    gastar = 60000
    comprar = 11
    print("Se va a gastar: ", gastar, "$ en la camiseta de 60000")    
     
#de 62000 a 64999
if presupuesto >= 62000 and presupuesto < camisetas[2] + pelotas[0] and comprar == 0:
    gastar = 62000
    comprar = 12
    print("Se va a gastar: ", gastar, "$ en la camiseta de 50000 + la pelota de 12000")  

#de 65000 a 67999   
if presupuesto >= 65000 and presupuesto < camisetas[2] + pelotas[1] and comprar == 0:
    gastar = 65000
    comprar = 13
    print("Se va a gastar: ", gastar, "$ en la camiseta de 60000 + la pelota de 5000")      

#de 68000 a 71999
if presupuesto < camisetas[2] + pelotas[2] and presupuesto >= camisetas[2] + pelotas[1] and comprar == 0:
    gastar = pelotas[1] + camisetas[2]
    comprar = 14
    print("Se va a gastar: ", gastar, "$ en la camiseta de 60000 + la pelota de 8000")     
       
#de 72000 hacia arriba    
if presupuesto >= camisetas[2] + pelotas[2] and comprar == 0:
    gastar = pelotas[2] + camisetas[2]
    comprar = 15
    print("Se va a gastar: ", gastar, "$ en la camiseta de 60000 + la pelota de 12000")
    
