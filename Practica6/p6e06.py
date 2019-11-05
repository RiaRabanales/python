'''Maria Rabanales: P6E6
Escribe un programa que pida primero dos números (máximo y mínimo) y luego
números intermedios. Para terminar de escribir números, escribe un número
que no esté comprendido entre los dos valores iniciales. El programa termina
escribiendo la lista de números.'''

nummin = int(input("Escribe un numero entero: "))
nummax = int(input("Escribe otro numero entero mayor que %d: " %(nummin)))
while nummin > nummax:
    nummax = int(input("%d no es mayor que %d. Vuelve a probar: " %(nummax, nummin)))

listnum = []
condicion = True

while condicion == True:
    nummid = int(input("Escribe un numero entre %d y %d: " %(nummin, nummax)))
    if (nummin < nummid) and (nummid < nummax):
        listnum.append(nummid)
    else:
        condicion = False

print("Los numeros entre %d y %d que has escrito son:" %(nummin, nummax))
for i in range(len(listnum)):
    print(listnum[i], end=" ")
