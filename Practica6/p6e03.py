'''Maria Rabanales: P6E3
Escribe un programa que pida notas y los guarde en una lista.
Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10.
El programa termina escribiendo la lista de notas.'''

print("Ahora introduciremos notas.\nSi introduces una nota imposible el programa acabará.")

listanotas = []
nota = 0

while (nota >= 0) and (nota <= 10):
    nota = float(input("Escribe una nota: "))
    if (nota >= 0) and (nota <= 10):
        listanotas.append(nota)

print("Las notas que has escrito son ",listanotas)









'''Esta version me incluye el ultimo valor:

while ((nota>=0) and (nota<=10)):
    nota=input("Escribe una nota: ")
    listanotas.append(nota)

print("Las notas que has escrito son ",listanotas)'''
    
