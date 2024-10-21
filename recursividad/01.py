import os
os.system("cls")

# Ejemplo 1: Suma de elementos de una lista

def sumaLista(lista) :
    if len(lista) == 0 :
        return 0
    else :
        return lista[0] + sumaLista(lista[1:])

lista = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
resultado = sumaLista(lista)

print(f"La suma de los elementos de la lista es: {resultado}")