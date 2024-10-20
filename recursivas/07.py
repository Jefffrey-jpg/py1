import os
os.system("cls")

# Ejemplo 7: Verificar un número primo

def esPrimo(n, divisor=2) :
    if n <= 1 :
        return False
    if divisor * divisor > n :
        return True
    if n % divisor == 0 :
        return False
    return esPrimo(n, divisor + 1)

n = int(input("Ingrese un número entero positivo: "))
resultado = esPrimo(n)

print(f"¿El número {n} es primo?: {resultado}")