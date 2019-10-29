#Maria Rabanales - P5 E11: divisores

num1=int(input("Dame un numero entero: "))

print("Los divisores de",num1,"son:")
for i in range (1,num1):
    if (num1%i==0):
        print(i)
