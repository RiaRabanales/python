'''Maria Rabanales: P7E12a
Escribir un programa que lea una frase, y pase ésta como parámetro a una
función que debe contar el número de palabras que contiene. Debe imprimir
el programa principal el resultado. Asumir que cada palabra está separada
por un solo blanco.'''


def separarPalabras(a):
    cuenta = 1
    #porque cuento las palabras previamente: esta es la inicial
    for i in range(0, len(a)):
        if a[i] == " ":
            cuenta += 1
    i += 1
    return ("Esta frase tiene %d palabras." % (cuenta))

frase = input("Escribe una frase con las palabras separadas por un solo espacio:\n")
print("¡Gracias!", separarPalabras(frase))
