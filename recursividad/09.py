import os
os.system("cls")

# Ejemplo 9: Encontrar el número máximo

def encontrar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    max_resto = encontrar_maximo(lista[1:])
    return lista[0] if lista[0] > max_resto else max_resto

lista = list(map(int, input("Ingrese números separados por espacios: ").split()))
resultado = encontrar_maximo(lista)

print(f"El valor máximo en la lista es: {resultado}")