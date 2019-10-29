#Maria Rabanales - P5 E2: pedir dos numeros y dar pares/impares

numa=int(input("Escribe un numero entero: "))
numb=int(input("Escribe otro numero entero mayor: "))

for i in range(numa, numb+1):
    if (i%2==0):
        print("El numero",i,"es par.")
    else:
        print("El numero",i,"es impar.")
