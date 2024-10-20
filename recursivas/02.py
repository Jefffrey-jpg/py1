import os
os.system("cls")

# Ejemplo 2: Invertir una cadena

def invertir(cadena) :
    if len(cadena) == 0 :
        return ""
    else :
        return cadena[-1] + invertir(cadena[:-1])

cadena = input("Ingrese una cadena: ")
resultado = invertir(cadena)

print(f"Cadena invertida: {resultado}")