import os
os.system("cls")

minutos = float(input("Ingresar duración de la llamada en minutos: "))
costoPorMinuto = 0.5

if minutos > 3:
    costoTotal = 3 * costoPorMinuto + (minutos - 3) * 0.2
else:
    costoTotal = minutos * costoPorMinuto

print(f"Costo total de la llamada: {costoTotal}")