import os
os.system("cls")

numero = input("Ingrese un numero de 4 cifras: ")

if len(numero) == 4 and numero.isdigit():
    numeroInvertido = numero[::-1]
    print(f"Número al revés: {numeroInvertido}")
else:
    print("El numero no tiene 4 cifras.")