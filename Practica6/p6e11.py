'''Maria Rabanales - P06E11
Escribir un programa para jugar a adivinar un número. El programa empieza
pidiendo entre qué números está el número a adivinar, se "inventa" un número
al azar y luego el usuario va probando valores. El programa va decidiendo si
son demasiado grandes o pequeños.'''



print("Juguemos a un juego.")
minimo = int(input("Escribe valor mínimo: "))
maximo = int(input("Escribe valor máximo: "))

import random
import time
random.seed(time.time())
adivinado = random.randint(minimo,maximo)
contador = 0

print("A ver si adivinas un número entero entre %d y %d." %(minimo,maximo))
num0 = int(input("Escribe un número: "))

while num0 != adivinado:
    if num0 > adivinado:
        contador = contador + 1
        num0 = int(input("Demasiado grande. Vuelve a intentarlo: "))
    if num0 < adivinado:
        contador = contador + 1
        num0 = int(input("Demasiado pequeño. Vuelve a intentarlo: "))

if contador = 1:
    print("Correcto; lo has intentado %d vez." %(contador))  
else:
    print("Correcto; lo has intentado %d veces." %(contador))    
