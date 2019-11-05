'''Maria Rabanales: P6E2
Escribe un programa que te pida números y los guarde en una lista.
Para terminar de introducir número, simplemente escribe “Salir”.
El programa termina escribiendo la lista de números.'''

#preguntar: existe do/while en python? me aseguro de al menos una iteracion...

listanum = []
condicion = "cualquiera"

while condicion != "Salir":
    num1 = int(input("Escribe un numero entero: "))
    listanum.append(num1)
    condicion = input("Si no quieres añadir mas numeros, escribe \'Salir\'.\n")

print("Lista de numeros: ",listanum)
