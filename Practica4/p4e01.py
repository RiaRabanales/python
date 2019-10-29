#Maria Rabanales - P4 E1. De 5 numeros, decir mayor y menor


a,b,c,d,e = int(input("Escribe un numero entero: ")),\
           int(input("Ahora escribe un segundo numero entero: ")),\
           int(input("Ahora escribe un tercer numero entero: ")), \
           int(input("Ahora escribe un cuarto numero entero: ")), \
           int(input("Ahora escribe un quinto numero entero: "))
print("Los numeros introducidos son: ",a,",",b,",",c,",",d,",",e)

maxim = a
if (b > maxim):
    maxim = b
if (c > maxim):
    maxim = c
if (d > maxim):
    maxim = d
if (e > maxim):
    maxim = e
print("El mayor valor es",maxim)

minim = a
if (b < minim):
    minim = b
if (c < minim):
    minim = c
if (d < minim):
    minim = d
if (e < minim):
    minim = e
print("El menor valor es",minim)
