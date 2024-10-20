import os
os.system("cls")

# Ejemplo 4: Producto de los números en una lista

def producto(lista):
    if len(lista) == 0:
        return 1
    else:
        return lista[0] * producto(lista[1:])

lista = [int(x) for x in input("Ingrese números separados por espacio: ").split()]
resultado = producto(lista)

print(f"El producto de los elementos de la lista es: {resultado}")