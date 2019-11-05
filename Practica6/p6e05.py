'''Maria Rabanales: P6E5
Escribe un programa que te pida números cada vez más grandes y que se guarden en una
lista. Para acabar de escribir los números, escribe un número que no sea mayor que
el anterior. El programa termina escribiendo la lista de números.'''

milista = []
num1 = int(input("Escribe un numero: "))
milista.append(num1)

num2 = int(input("Escribe un numero mayor que %d: " %(milista[0])))
if num2 > num1:
    milista.append(num2)
    while milista[-1] > milista[-2]:
        num3 = int(input("Escribe un numero mayor que %d: " %(milista[-1])))
        milista.append(num3)

#tengo que quitar el ultimo valor del while, que sera menor:
del milista[-1]

print("Los numeros que has escrito son:")
for i in range(len(milista)):
    print(milista[i], end="  ")
