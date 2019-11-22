'''Maria Rabanales: P7E5
Escribe un programa que te pida una frase y una vocal, y pase estos datos
como parámetro a una función que se encargará de cambiar todas las vocales
de la frase por la vocal seleccionada. Devolverá la función la frase modificada,
y el programa principal la imprimirá.
'''

def cambioVocal(frase,vocal):
    frase = frase.replace("a", vocal)
    frase = frase.replace("e", vocal)
    frase = frase.replace("i", vocal)
    frase = frase.replace("o", vocal)
    frase = frase.replace("u", vocal)
    return frase

frase = input("Escribe una frase:\n")
vocal = input("¿Cuál es tu vocal favorita? ")
while vocal != "a" and vocal != "e" and vocal != "i" and vocal != "o" and vocal != "u":
    vocal = input("Eso no es una vocal. Escribe una vocal, anda: ")
print(cambioVocal(frase,vocal))
