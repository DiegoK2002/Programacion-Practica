# Límite de n = 209  

n = int(input("Ingrese un n: ", ))

i = "*"
j = "*"
l = "*"
b = n - 2
maxi = n
doble_max = 0
z = 0
k = n - 1

while z < maxi:
    print(i)
    i = i + j
    z = z + 1
while k > doble_max:
    l = "*" + b * "*"
    print(l)
    b = b - 1
    k = k - 1
    
    
    
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *