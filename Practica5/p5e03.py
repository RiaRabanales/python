#Maria Rabanales - P5 E3: pedir dos numeros y dar suma de enteros


numa=int(input("Escribe un numero entero: "))
numb=int(input("Escribe otro numero entero mayor que el anterior: "))

sumab=numa
for i in range (numa+1,numb+1):
    sumab=sumab+i
print("La suma desde",numa,"hasta",numb,"es igual a",sumab)
