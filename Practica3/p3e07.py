#Maria Rabanales - P3 E7: pedir y validar una fecha

any = int(input("A continuacion te pedire una fecha.\n Introduce el año en numeros: "))
mes = int(input(" Introduce el mes en numeros: "))
dia = int(input(" Introduce el numero del dia: "))

if (any<1) or (any>9999):
    print("Año invalido.")
elif (mes<1) or (mes>12):
    print("Mes invalido.")
elif (dia<1) or (dia>31):
    print("Dia invalido.")
elif ((mes==4) or (mes==6) or (mes==9) or (mes==11)) and (dia>30):
    print("Dia invalido.")
elif (mes==2):
    if (any%4==0) and (dia>29):
        print("Dia invalido.")
    elif (dia>28):
        print("Dia invalido.")
else:
    print("Fecha correcta: %d/%d/%d." % (dia,mes,any))
