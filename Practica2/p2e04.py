#Maria Rabanales - P2 E4: Calcular el mayor de dos numeros

A = int(input('Dame un numero entero: '))
B = int(input('Ahora dame otro numero entero: '))
if A > B:
    print('El primer numero es mayor.')
elif (A == B):
    print('Los dos numeros son iguales.')
else:
    print('El ultimo numero es mayor.')
print('Fin de la comparacion.')
