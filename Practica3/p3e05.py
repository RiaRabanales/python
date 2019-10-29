#Maria Rabanales - P3 E5. Pedir numero y evaluar validez


nume = int(input("Escribe un numero entero con un maximo de tres cifras: "))
if (nume>999):
    print("Tu numero no cumple los requisitos solicitados.")
else:
    print("Gracias por compartir el numero",nume,".")
