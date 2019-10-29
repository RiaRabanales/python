#Maria Rabanales - P4 E5. Devolucion de billetes exactos.

importe = int(input("Escribe el dinero que quieres cambiar, sin centimos: "))

if (importe%500 == 0):
    print("El cajero te devuelve",(importe//500),"billetes de 500 euros.")
elif (importe%200 == 0):
    print("El cajero te devuelve",(importe//200),"billetes de 200 euros.")
elif (importe%100 == 0):
    print("El cajero te devuelve",(importe//100),"billetes de 100 euros.")
elif(importe%50 == 0):
    print("El cajero te devuelve",(importe//50),"billetes de 50 euros.")
elif(importe%20 == 0):
     print("El cajero te devuelve",(importe//20),"billetes de 20 euros.")
elif(importe%10 == 0):
     print("El cajero te devuelve",(importe//10),"billetes de 10 euros.")
elif(importe%5 == 0):
     print("El cajero te devuelve",(importe//5),"billetes de 5 euros.")
else:
    print("El cajero no te puede devolver un unico tipo de billete.")
