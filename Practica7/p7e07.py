'''Maria Rabanales: P7E7
Escribe un programa que lea una frase, y la pase como parámetro a un
procedimiento. El procedimiento contará el número de vocales (de cada una)
que aparecen, y lo imprimirá por pantalla.
'''

def contarVocales(frase):
    anumb = 0
    enumb = 0
    inumb = 0
    onumb = 0
    unumb = 0
    for i in range(0,len(frase)):
        if frase[i] == "a":
            anumb+=1
        elif frase[i] == "e":
            enumb+=1
        elif frase[i] == "i":
            inumb+=1
        elif frase[i] == "o":
            onumb+=1
        elif frase[i] == "u":
            unumb+=1
    print("Tu frase tiene %d veces la vocal a, %d e, %d i, %d o, y %d u." %(anumb,enumb,inumb,onumb,unumb))


frase = input("Escribe una frase: ")
contarVocales(frase.lower())
            
