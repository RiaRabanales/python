#Maria Rabanales - P5 E10: triangulo raro

alto=int(input("Escribe la altura del triangulo en cm enteros: "))
print("La representacion grafica de este triangulo es:")
for i in range(0, alto):
    print(' '*(alto-i),'*'*(i+(i+1)))

