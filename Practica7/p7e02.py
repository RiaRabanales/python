'''Maria Rabanales: P7E2
Escribe un programa que lea el nombre y los dos apellidos de una persona
(en tres cadenas de caracteres diferentes), los pase como parámetros a una
función, y ésta debe unirlos y devolver una única cadena. La cadena final
la imprimirá el programa por pantalla.'''

def unificarNombre(a, b, c):
    nombrecompleto = (a.capitalize()+" "+b.capitalize()+" "+c.capitalize())
    return nombrecompleto

print("Introduce tus siguientes datos:")
nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ")

print("Unificando, eres", end=": ")
print(unificarNombre(nombre,apellido1,apellido2))
