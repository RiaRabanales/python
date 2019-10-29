#Maria Rabanales - P5 E4: dar el factor de un numero


num1=int(input("Escribe un numero entero: "))

factor=num1
for i in range (num1-1,0,-1):
    factor=factor*i
print("El factorial de",num1,"es",factor)
