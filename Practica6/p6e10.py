'''Maria Rabanales: P6E10
Escribe un programa que te pida los nombres y notas de alumnos. Si escribes
una nota fuera del intervalo de 0 a 10, el programa entenderá que no quieres
introducir más notas de este alumno. Si no escribes el nombre, el programa
entenderá que no quieres introducir más alumnos.'''

print("Necesito los nombres de tus alumnos y al menos una nota valida.\n" +
      "Si escribes una nota imposible cambiara el alumno.\n" +
      "Si no escribes nombre se cerrara el programa.")
lista = []
nombre = " "

while nombre != "":
    nombre = input("Escribe un nombre: ")
    listalumno = []
    if nombre != "":
        listalumno.append(nombre)
        nota = int(input("Escribe una nota: "))
        listalumno.append(nota)
        while nota >= 0 and nota <= 10:
            nota = int(input("Escribe otra nota: "))
            if nota >= 0 and nota <= 10:
                listalumno.append(nota)
        lista.append(listalumno)
                

print("Las notas de los alumnos son:")
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j == 0:
            print(lista[i][j], end = ": ")
        elif j == (len(lista[i])-1):
            print(lista[i][j], end = "\n")
        else:
            print(lista[i][j], end = ", ")
     
