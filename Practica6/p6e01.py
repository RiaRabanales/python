'''Maria Rabanales: P6E1
Escribe un programa que te pida palabras y las guarde en una lista.
Para terminar de introducir palabras, simplemente pulsa Enter.
El programa termina escribiendo la lista de palabras.'''

lista1 = []
palabra = " "

while (palabra != ""):
    palabra = input("Escribe la palabra que quieras añadir: ")
    if (palabra != ""):
        lista1.append(palabra)

print("Las palabras que has escrito son", end = " ")
for i in range(len(lista1)):
    if i == len(lista1)-1:
        print(lista1[i])
    else:
        print(lista1[i], end = ", ")






'''Solucion de Rafa para el do/while:

palabras=[]
entrada=input("Pasame una palabra: ")
while(entrada!=""):
    palabras.append(entrada)
    entrada=input("Pasame una palabra: ")
print("La lista de palabras es",palabras)
'''
