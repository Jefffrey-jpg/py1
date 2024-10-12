import os
os.system("cls")

numero = input("Número de 4 cifras: ")

numeroReves = numero[::-1]

resultado = (len(numero) == 4) * f"Número al revés: {numeroReves}" + (len(numero) != 4) * "El número no tiene 4 cifras."

print(resultado)