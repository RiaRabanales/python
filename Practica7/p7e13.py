'''Maria Rabanales: P7E13
Escribe un programa que le pida al usuario si quiere calcular si un número es
primo con for o con while, por tanto, habrá dos funciones que se caracterizan
por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra
(con while). Ambas funciones devolverá true (si es es primo) o false (si no
es primo). El programa principal informará del resultado. Además, como mejora
puedes calcular el tiempo que tarda en encontrar la solución de una manera u
otra. Comentario: aprovecha el código que tienes ya creado.'''

import time
    
def calcularFor(num):
    primo = True
    for i in range (2,num):
        if num%i != 0:
            primo = False
    return primo

def calcularWhile(num):
    primo = False
    i = 2
    while num%i != 0 and primo == False:
        i += 1
        if i == num:
            primo == True
    return primo


numero = int(input("Introduce un número entero: "))
metodologia = input("Dime cómo quieres ver si es primo. \n" +
                    "Escribe F para for, y W para while.\n")
esPrimo = False
start_time = time.time_ns()
if metodologia == "f" or metodologia == "F":
    esPrimo = calcularFor(numero)
elif metodologia == "w" or metodologia == "W":
    esPrimo = calcularWhile(numero)
end_time = time.time_ns()
print(" ---- ", end_time-start_time, "nanosegundos")

if esPrimo == False:
    print("El número %d no es primo." %(numero))
else:
    print("El número %d es primo." %(numero))
