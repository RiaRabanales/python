#Maria Rabanales - P3 E6 - Pedir producto y precio y dar precio con IVA.


nombre = input("Introduce el nombre de tu producto: ")
precio = float(input("Introduce el precio del producto, en euros y formato X.XX: "))
precioiva = (precio*1.21)
print("Tu %s tiene un precio base de %f euros y un precio con IVA de %f euros." % (nombre,precio,precioiva))
