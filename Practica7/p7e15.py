'''Maria Rabanales: P7E15
Desarrolla un programa utilizando la metodología “pair programming”, que nos
sirva para gestionar nuestros contactos (la información a gestionar será el
teléfono, nombre, apellido1, apellido2 y correo electrónico. El programa
tendrá un menú, con las siguientes opciones: añadir contacto, consultar
contacto a partir de la clave, consultar todos los contactos y eliminar
contacto.'''


def agregarcontacto():
    contacto = {}
    print("Introduce la siguiente información:")
    yacontacto = True
    while yacontacto == True:
        contacto["telef"] = input("Número de teléfono (sin espacios): ")
        if buscarcontacto(contacto["telef"]) == True:
            print("Este teléfono ya existe. Probemos de nuevo.")
            yacontacto = True
        else:
            contacto["nombre"] = input("Nombre: ")
            contacto["apellido1"] = input("Primer apellido: ")
            contacto["apellido2"] = input("Segundo apellido: ")
            contacto["email"] = input("Correo electrónico: ")
            yacontacto = False
    return contacto

def veragenda():
    for i in range(len(agenda)):
        vercontacto(agenda[i])

def vercontacto(contacto):
    print("Teléfono:", contacto["telef"], end = " - ")
    print("Nombre:", contacto["nombre"], end = " - ")
    print("Apellidos:", contacto["apellido1"], contacto["apellido2"], end = " - ")
    print("E-mail:", contacto["email"])

def buscarcontacto(numtelef):
    telefencontrado = False
    for i in range(len(agenda)):
    #esto rechina. "for contacto in agenda" sería más limpio quizás¿? pensar.
        if numtelef in agenda[i]["telef"]:
            vercontacto(agenda[i])
            telefencontrado = True
        # i+=1 no me hace falta, me aumenta el contador él solo
    return telefencontrado

def borrarcontacto(numtelef):
    for i in range(len(agenda)):
        if numtelef in agenda[i]["telef"]:
            agenda[i].clear()
            print("Contacto eliminado")

agenda = []
salir = False
while not salir:
    print("¿Qué deseas hacer?")
    print("  1. Introducir un nuevo contacto")
    print("  2. Ver todos los contactos existentes")
    print("  3. Buscar teléfono en los contactos existentes")
    print("  4. Borrar un contacto de la agenda")
    print("  0. Salir\n")
    accion = input("Introduce tu opción: ")
    if accion == "1":
        contacto = agregarcontacto()
        agenda.append(contacto)
    elif accion == "2":
        veragenda()
    elif accion == "3":
        telefbusqueda = input("Escribe el teléfono que quieres buscar: ")
        #completar con busqueda por los demas factores quizas¿?
        buscarcontacto(telefbusqueda)
    elif accion == "4":
        telefbusqueda = input("Escribe el teléfono que quieres borrar: ")
        if buscarcontacto(telefbusqueda) == False:
            print("Este teléfono no existe")
        else:
            borrarcontacto(telefbusqueda)
    elif accion == "0":
        print("ADIOS BABUINO!!!")
        salir = True
    else:
        print("Opción imposible; prueba de nuevo.")
