'''Maria Rabanales: P7E14
Aprovechando el potencial de los diccionarios, escribe un programa que llame
a un procedimiento, que recibe como parámetro la fecha en números y devuelve
la fecha  con el nombre del mes. Comentario: no es necesario validar si la es
correcta, damos por hecho que lo será.'''


def decirMes (fecha):
    dia = fecha[0:2]
    mes = fecha[3:5]
    anyo = fecha[6:]
    meses = {"01": "enero",
           "02": "febrero",
           "03": "marzo",
           "04": "abril",
           "05": "mayo",
           "06": "junio",
           "07": "julio",
           "08": "agosto",
           "09": "septiembre",
           "10": "octubre",
           "11": "noviembre",
           "12": "diciembre"}
    nombremes = meses[mes] 
    print(dia, "de", nombremes, "del año", anyo)

fechauser = input("Introduce la fecha en formato DD/MM/AAAA." +
                  "\nRecuerda separar con barras.\n")
decirMes(fechauser)
