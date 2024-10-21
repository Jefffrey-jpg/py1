import os
os.system("cls")

# Ejemplo 5: Buscar un elemento en una lista

def busqueda(lista, elemento) :
    if len(lista) == 0 :
        return False
    elif lista[0] == elemento :
        return True
    else :
        return busqueda(lista[1:], elemento)

lista = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
elemento = int(input("Ingrese el elemento a buscar: "))
resultado = busqueda(lista, elemento)

print(f"¿El elemento {elemento} está en la lista?: {resultado}")