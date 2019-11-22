'''Maria Rabanales: P7E3
Escribe un programa que lea una frase, y la pase como parámetro a un
procedimiento, y éste debe mostrar la frase con un carácter en cada línea.'''

def imprimirCadena(cadena):
    for i in range(len(cadena)):
        print(cadena[i])
        i+=1

frase = input("Escribe una frase:\n")
imprimirCadena(frase)
