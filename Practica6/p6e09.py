'''Maria Rabanales: P6E9
Escribe un programa que te pida nombres de personas y sus números de teléfono.
Para terminar debe pulsar “S” cuando te pida el nombre. El programa termina
escribiendo nombres y números de teléfono en una lista de listas.'''

print("Cuando quieras parar, escribe \'S\' en un nombre.")

nombre = ""
telf = 0
lista = []

while (nombre != "S"):
    nombre = input("Dame un nombre: ")
    if (nombre != "S"):
        telf = int(input("Dame su telefono: "))
        lista.append([nombre, telf])

print("Los nombres y telefonos de la agenda son: ")
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j == 0:
            print(lista[i][j], end=": ")
        if j == 1:
            print(lista[i][j])
