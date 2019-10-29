#Maria Rabanales - P4 E2. De 5 numeros, decir orden


a,b,c,d,e = int(input("Escribe un numero entero: ")),\
           int(input("Ahora escribe un segundo numero entero: ")),\
           int(input("Ahora escribe un tercer numero entero: ")),\
           int(input("Ahora escribe un cuarto numero entero: ")),\
           int(input("Ahora escribe un quinto numero entero: "))
print("Los numeros introducidos son: ",a,",",b,",",c,",",d,",",e)

if ((a>b) and (b>c) and (c>d) and (d>e)):
    print("Estos numeros estan en orden decreciente.")
elif ((a<b) and (b<c) and (c<d) and (d<e)):
    print("Estos numeros estan en orden creciente.")
else:
    print("Estos numeros estan desordenados.")

