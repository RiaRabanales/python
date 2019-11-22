'''Maria Rabanales: P7E4
Escribe un programa que pida una frase, y le pase como parámetro a una función
dicha frase. La función debe sustituir todos los espacios en blanco de una
frase por un asterisco, y devolver el resultado para que el programa principal
la imprima por pantalla.'''

#Versión fácil con replace:
def imprimirCadena(cadena):
    cadenaimpresa = cadena.replace(" ", "*")
    return cadenaimpresa

frase = input("Escribe una frase:\n")
print(imprimirCadena(frase))



'''Version mas complicada: ver al final
def imprimirCadena(cadena):
    cadenaimpresa = ""
    for i in range(len(cadena)):
        if (cadena[i]) == " ":
            cadenaimpresa.join("*")
        else:
            cadenaimpresa.join(cadena[i])
        i+=1
    return cadenaimpresa

frase = input("Escribe una frase:\n")
print(imprimirCadena(frase))
'''



