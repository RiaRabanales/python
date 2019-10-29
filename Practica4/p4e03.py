#Maria Rabanales - P4 E3. Areas de triangulo y cuadrado.

figura = input("Calculemos un area.\nEscribe \'triangulo\' si quieres calcular el area de un triangulo.\nEscribe \'rectangulo\' si quieres calcular el area de un rectangulo.\nRecuerda que un cuadrado es un tipo de rectangulo en que base=altura.\nAhora, escribe:\n")

if (figura != "triangulo") and (figura != "rectangulo"):
    print("No podemos calcular el area de esta cosa.")

else:
    base = int(input("Escribe la base en cm y con formato de numero entero: "))
    altura = int(input("Ahora escribe la altura en cm y con formato de numero entero: "))

    if (figura == "triangulo"):
        area = (base*altura)/2
        print("Este triangulo mide",area,"cm2 de area.")
    else:
        area = (base*altura)
        print("Este rectangulo mide",area,"cm2 de area.")
        if (base == altura):
            print("Además, este rectángulo es un cuadrado.")

    
