#Maria Rabanales - P5 E8: triangulo


ancho=int(input("Escribe la anchura del triangulo en cm enteros: "))
print("La representacion grafica de este triangulo es:")
for i in range(1, ancho):
    print('*'*i)
for i in range(ancho, 0, -1):
    print('*'*i)
