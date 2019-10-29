"""Maria Rabanales - P5 E12
Ver si un numero es primo."""

num1=int(input('Escribe un numero entero: '))
primo=True

for i in range(2,num1):
    if (num1%i==0):
        primo=False

if (primo==False):
    print('El numero', num1, 'no es primo.')
else:
    print('El numero', num1, 'es primo.')



#i=0
#while num1%i!=0:
#   i+=1
   
