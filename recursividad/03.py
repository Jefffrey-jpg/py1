import os
os.system("cls")

# Ejemplo 3: Contar los dígitos de un nmúmero

def contarDigitos(numero) :
    if numero == 0 :
        return 0
    else :
        return 1 + contarDigitos(numero // 10)

numero = int(input("Ingrese un número entero: "))
resultado = contarDigitos(numero)

print(f"La cantidad de dígitos en el número es: {resultado}")