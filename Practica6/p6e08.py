'''Maria Rabanales: P6E8
Escribe un programa que te pida primero un número y luego te pida números hasta
que la suma de los números introducidos coincida con el número inicial.
El programa termina escribiendo la lista de números.'''


numlimit = int(input("Escribe un número límite: "))
num1 = int(input("Escribe un valor: "))
listanum = []
sumanum = 0

while  (sumanum < numlimit):
    if ((sumanum + num1) > numlimit):
        num1 = int(input("El número %d es demasiado grande. Escribe otro número: "))
    else:
        sumanum = sumanum + num1
        listanum.append(num1)
        if (sumanum < numlimit):
            num1 = int(input("Escribe otro valor: "))

print("Has alcanzado el límite de", numlimit, " y la lista creada es:", end = " ")
for i in range(len(listanum)):
    print(listanum[i], end = " ")








'''
while (sumanum < num0):
    num1 = int(input("Escribe otro valor: "))
    listanum.append(num1)
    sumanum = sumanum + num1

if (sumanum == num0):
    print("El limite a alcanzar es",num0,"y la lista creada es:")
    for i in range(len(listanum)):
        print(listanum[i])
        
if (sumanum > num0):
    del listanum[-1]
    print(num1,"es demasiado grande.")
    sumanum = sumanum - num1
    while (sumanum < num0):
        num1 = int(input("Escribe otro valor: "))
        if ((sumanum + num1) == num0):
            listanum.append(num1)
            sumanum = sumanum + num1
            print("El limite a alcanzar es",num0,"y la lista creada es:")
            for i in range(len(listanum)):
                print(listanum[i])
        elif ((sumanum + num1) < num0):
            sumanum = sumanum + num1
            listanum.append(num1)
        if ((sumanum + num1) > num0):
            print(num1,"es demasiado grande.")
'''






'''
while (sumanum < num0):
    num1 = int(input("Introduce un valor: "))
    listanum.append(num1)
    sumanum = sumanum + num1

if (sumanum != num0):
    sumanum = sumanum - num1
    del listanum[-1]
    while ((sumanum + num1) > num0):
        num1 = int(input("Este numero es demasiado grande. Escribe otro valor: "))
'''
