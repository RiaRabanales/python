#Maria Rabanales - P4 E4. Cuarto numero divisor (contenido un num exacto de veces) de tres anteriores.

num1 = int(input("Vamos a hacer un ejercicio de división.\nDame un primer numero entero: "))
num2 = int(input("Dame un segundo numero entero: "))
num3 = int(input("Dame un tercer numero entero: "))
num4 = int(input("Dame un ultimo numero entero: "))

if ((num1%num4 == 0) and (num2%num4 == 0) and (num3%num4 == 0)):
    print(num4,"es divisor de los otros tres numeros.")
else:
    print(num4,"no es divisor de los otros tres numeros.")
    
