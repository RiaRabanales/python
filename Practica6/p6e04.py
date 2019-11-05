'''Maria Rabanales: P6E4
Escribe un programa que te pida dos números, el segundo mayor que el primero.
El programa termina escribiendo los dos números.'''

num1 = int(input("Escribe un numero entero: "))
num2 = int(input("Escribe un numero mayor que %d: " %num1))

while num1 >= num2:
    num2 = int(input("%d no es mayor que %d." %(num2,num1) +
                   " Vuelve a introducir un numero: "))

print("Los numeros que has escrito son %d y %d." %(num1,num2))
                   
