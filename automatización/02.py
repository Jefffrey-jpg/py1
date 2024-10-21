import os
os.system("cls")

# Conversor de unidades

def convertir_unidad():
    unidad = input("Unidad a convertir (km a millas/Celsius a Fahrenheit): ").lower()
    valor = float(input("Valor a convertir: "))

    if unidad == "km a millas":
        resultado = valor * 0.621371
        print(f"{valor} km son {resultado} millas.")
    elif unidad == "celsius a fahrenheit":
        resultado = (valor * 9/5) + 32
        print(f"{valor}°C son {resultado}°F.")
    else:
        print("Unidad no válida.")

convertir_unidad()