'''Maria Rabanales: P6E7
Escribe un programa que pida un número (límite) y luego te pida números hasta
que la suma de los números introducidos supere el límite inicial. El programa
termina escribiendo la lista de números.'''

numlim = int(input("Escribe un numero limite: "))
lista = []
sumalista = 0

while (sumalista < numlim):
    numadd = int(input("Escribe un valor: "))
    lista.append(numadd)
    sumalista = sumalista + lista[-1]

print("El limite a superar es %d. La suma de los numeros es %d. Los numeros en la lista son:" %(numlim,sumalista))
for i in range(len(lista)):
      print(lista[i], end=" ")
