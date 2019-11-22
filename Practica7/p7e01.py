'''Maria Rabanales: P7E1
Escribe un programa que pida un texto por pantalla, este texto lo pase
como parámetro a un procedimiento, y éste lo imprima primero todo en
minúsculas y luego todo en mayúsculas.'''

def editarTexto(cadena):
    print(cadena.upper())
    print(cadena.lower())

texto = input("Escribe un texto:\n")
editarTexto(texto)
