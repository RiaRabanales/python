'''Maria Rabanales: P7E9
Escribe un programa que pida dos palabras las pase como parámetro a un
procedimiento y diga si riman o no. Si coinciden las tres últimas letras
tiene que decir que riman. Si coinciden sólo las dos últimas tiene que
decir que riman un poco y si no, que no riman.
'''

def decidirRima(a,b):
    if a[-1] == b[-1] and a[-2] == b[-2]:
        if a[-3] == b [-3]:
            print("¡Esto rima!")
        else:
            print("Esto rima un poco...")
    else:
        print("Esto no rima nada...")


frase1 = input("Escribe una palabra: ")
frase2 = input("Escribe otra palabra: ")
decidirRima(frase1,frase2)
