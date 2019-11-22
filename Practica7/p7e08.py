'''Maria Rabanales: P7E8
Escribe un programa que pida una frase, y pase la frase como parámetro a una
función que debe eliminar los espacios en blanco (compactar la frase). El
programa principal imprimirá por pantalla el resultado final.
'''

def quitarEspacios(a):
    '''volver aqui mas adelante y probar version:
    for i in range(0,len(a)):
        if a[i] == " ":
            a = a[0:i]+a[i+1:]
        else:
            i+=1'''

    #version facil:
    a = a.replace(" ","")
    return a

frase = input("Escribe una frase:\n")
print(quitarEspacios(frase))
