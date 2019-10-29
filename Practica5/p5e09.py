#Maria Rabanales - P5 E9: rectangulo

alto=int(input("Escribe la altura del rectangulo en cm enteros: "))
ancho=int(input("Escribe la anchura del rectangulo en cm enteros: "))
print("La representacion grafica de este rectangulo es:")
for i in range(1, alto+1):
    if ((i==1) or (i==alto)):
        print ('*'*ancho)
    else:
        print ('*',' '*(ancho-4),'*')
#Debiera usar (ancho-2), pero como python me añadirá dos espacios prefiero descontarlos.
#Podria evitar ese ancho-4 concatenando: print ('*'+' '*(ancho-2)+'*')
