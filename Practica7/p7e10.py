'''Maria Rabanales: P7E10
Escribe un programa que te pida una palabra o número, pase por parámetro estos
datos a una función, y ésta te diga si es o no palíndroma o capicúa. El
programa principal imprimirá el resultado de la función
'''

def verCapicua(a):
    capicua = True
    fraseretorno = ""
    while capicua == True and len(a)>1:
        if a[0] != a[-1]:
            capicua = False
        a = a[1:-1]
    if capicua == True:
        fraseretorno = "es capicúa o palíndroma."
    else:
        fraseretorno = "no es capicúa o palíndroma."
    return fraseretorno

inputusuario = input("Escribe algo: ")
print(inputusuario, verCapicua(inputusuario))
