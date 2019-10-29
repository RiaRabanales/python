#Maria Rabanales - P5 E5: rectangulo


alto=int(input("Escribe la altura del rectangulo en cm enteros: "))
ancho=int(input("Escribe la anchura del rectangulo en cm enteros: "))

print("La representacion grafica de este rectangulo es:")
for i in range(alto):
    print('*'*ancho)
