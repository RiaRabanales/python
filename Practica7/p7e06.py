'''Maria Rabanales: P7E6
Escribe un programa que lea el nombre de una persona y un carácter, le pase
estos datos a una función que comprobará si dicho carácter está en su nombre.
El resultado de dicha función lo imprimirá el programa principal por pantalla.
'''

#voy a probar con una nomenclatura de función diferente
def comprobarCaracter(a,b):
    resultado = "El carácter %s no está en %s" %(b,a)
    for i in range(0, len(a)):
        if (a[i] == b):
            resultado = "El carácter %s está en %s" %(b,a)
        i+=1 
    return resultado



nombre = input("Escribe tu nombre: ")
caracter = input("Escribe tu carácter favorito: ")
print(comprobarCaracter(nombre,caracter))
