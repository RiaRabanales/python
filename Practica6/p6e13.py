'''Maria Rabanales - P06E13
Desarrolla de nuevo el ejercicio de la práctica anterior de los números primos,
con while. Reflexiona y escribe en el propio programa en forma de comentario,
qué opción es mejor y por qué.
Escribe un programa que pida un número y escriba si primo o no.
'''

num1 = int(input('Escribe un numero entero: '))
i = 2
#No puedo iniciar i en 1 porque no me entraría en el while.
primo = False

while num1%i != 0 and primo == False:
    i+=1
    if i == num1:
        primo = True
        print("El número %d es primo." % (num1))

if primo == False:
    print("El número %d no es primo." % (num1))


'''Veo más adecuado esta versión con while que la versión con for del P5E12.
Con el while, en cuanto se encuentra un divisor se sale de la operación, con
lo que no hay iteraciones posteriores inútiles. Con el for, hay tantas iteraciones
como me indica el range, incluso cuando ya se ha determinado que el número no es
primo.
Con números pequeños no es muy obvio, pero con números grandes sí. Por ejemplo,
con '222675744' y while paro en la segunda iteración (porque es múltiplo de 2)
mientras que con for haría las 222675744 iteraciones a pesar de saber ya que no
es primo, y tardaría muchísimo.
'''
