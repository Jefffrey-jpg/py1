import os
os.system("cls")

# Ejemplo 10: Calcular el mínimo común múltiplo

def mcd(a, b) :
    if b == 0 :
        return a
    return mcd(b, a % b)

def mcm(a, b) :
    return abs(a * b) // mcd(a, b)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultado = mcm(a, b)

print(f"El Mínimo Común Múltiplo de {a} y {b} es: {resultado}")