'''Maria Rabanales: P7E11
Escribe un programa que te pida una frase, y pase la frase como parámetro a
una función. Ésta debe devolver si es palíndroma o no , y el programa principal
escribirá el resultado por pantalla.'''

def verPalindromo(a):
    palindromo = "si"
    fraseretorno = ""

    a = a.replace(" ", "")
    #originalmente he usado for i in range(0,len(a)) pero es peor que while
    if a.isalpha() == False:
        palindromo = "imposible"

    while palindromo == "si" and len(a)>1:
        if a[0] != a[-1]:
            palindromo = "no"
        a = a[1:-1]
            
    if palindromo == "si":
        fraseretorno = "es un palíndromo."
    elif palindromo == "no":
        fraseretorno = "no es un palíndromo."
    else:
        fraseretorno = "tiene números, así que no lo puedo analizar."
    return fraseretorno

inputusuario = input("Escribe algo: ")
print(inputusuario, verPalindromo(inputusuario))
#La diferencia con el anterior es que este sólo busca letras, no números.
