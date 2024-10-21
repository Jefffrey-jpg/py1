import os
os.system("cls")

# Ejemplo 8: Suma de cifras

def sumaCifras(numero):
    if numero == 0:
        return 0
    else:
        return (numero % 10) + sumaCifras(numero // 10)

numero = int(input("Ingrese un número entero: "))
resultado = sumaCifras(numero)
print(f"La suma de los dígitos del número es: {resultado}")