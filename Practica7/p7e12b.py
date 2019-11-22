'''Maria Rabanales: P7E12b
Escribir un programa que lea una frase, y pase ésta como parámetro a una
función que debe contar el número de palabras que contiene. Debe imprimir
el programa principal el resultado. No se sabe cómo están separadas las
palabras. Pueden estar separadas por más de un blanco o por signos de
puntuación.'''


def separarPalabras(a):
    buscapalabra = True
    cuentapalabra = 0
    for i in range(0, len(a)):
        #trace: print(buscapalabra,"   ",a[i:i+1].isalnum())
        if buscapalabra and a[i:i+1].isalnum():
            cuentapalabra += 1
            buscapalabra = False
        elif not buscapalabra and not a[i:i+1].isalnum():
            buscapalabra = True
        i += 1
    return ("Esta frase tiene %d palabras." % (cuentapalabra))

frase = input("Escribe una frase:\n")
print("¡Gracias!", separarPalabras(frase))






'''Idea: ¿y si saco a[i:i+1].isalnum() a una variable dentro del for para
hacer más legible el código?
ej:
esalfanum = a[i:i+1].isalnum
if buscapalabra and esalfanum:
... '''
