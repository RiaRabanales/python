'''Maria Rabanales - P06E12
Escribir un programa para jugar a adivinar un número.
El programa empieza pidiendo entre qué números está el número a adivinar.
Luego intenta adivinar de qué número se trata.
El usuario va diciendo si el número que ha dicho el programa es menor, mayor o
igual al que se ha buscado.
'''

import random

minimo = int(input("Decide un valor mínimo: "))
maximo = int(input("Decide un valor máximo: "))
print("Piensa un número entre %d y %d, a ver si lo puedo adivinar.\n" %(minimo,maximo))

pista = " "

while pista != "igual":
    prueba = random.randint(minimo,maximo)
    pista = input("¿Es %d? Escribe mayor, menor o igual: " %(prueba))
    if pista == "mayor":
        minimo = prueba+1;
    if pista == "menor":
        maximo = prueba-1;

print("¡%d! Gracias por jugar." %(prueba))
