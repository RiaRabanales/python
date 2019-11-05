'''Maria Rabanales - P06E12
Escribir un programa para jugar a adivinar un número.
El programa empieza pidiendo entre qué números está el número a adivinar.
Luego intenta adivinar de qué número se trata.
El usuario va diciendo si el número que ha dicho el programa es menor, mayor o
igual al que se ha buscado.
Mejoras (opcionales):
• que al principio el programa se asegure de que el valor máximo es superior.
• Que el programa detecte "trampas".
'''

import random

minimo = int(input("Decide un valor mínimo: "))
maximo = int(input("Decide un valor máximo: "))

while (maximo <= minimo):
    maximo = int(input("El numero no es mayor. Introduce algo mayor que %d: " %(minimo)))


print("Piensa un número entre %d y %d, a ver si lo puedo adivinar.\n" %(minimo,maximo))

pista = " "

while (pista != "igual") and (pista != "trampa"):
    prueba = random.randint(minimo,maximo)
    pista = input("¿Es %d? Escribe mayor, menor o igual: " %(prueba))
    if (pista != "mayor") and (pista != "menor") and (pista != "igual"):
        print("Esto no es lo que te he pedido...")
    if (pista == "mayor") and (prueba == maximo) or (pista == "menor") and (prueba == minimo):
        print("¡Tramposo!")
        pista = "trampa"
    else:
        if (pista == "mayor"):
            minimo = prueba+1;
        if (pista == "menor"):
            maximo = prueba-1;

if (pista == "igual"):
    print("¡%d! Gracias por jugar." %(prueba))
