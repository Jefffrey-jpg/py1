import os
os.system("cls")

# Ejemplo 6: Calcular una potencia

def potencia(base, exponente) :
    if exponente == 0 :
        return 1
    else :
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)

print(f"{base} elevado a {exponente} es: {resultado}")