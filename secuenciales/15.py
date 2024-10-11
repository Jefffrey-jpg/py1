import os
os.system("cls")

juanDolares = float(input("Ingrese la cantidad de Juan en dólares: "))
rosaDolares = float(input("Ingrese la cantidad de Rosa en dólares: "))
danielSoles = float(input("Ingrese la cantidad de Daniel en soles: "))

danielDolares = danielSoles / 3
capitalTotal = danielDolares + juanDolares + rosaDolares

porcentajeJuan = (juanDolares / capitalTotal) * 100
porcentajeRosa = (rosaDolares / capitalTotal) * 100
porcentajeDaniel = (danielDolares / capitalTotal) * 100

print(f"Capital total en dólares: {capitalTotal:.2f}")
print(f"Porcentaje de Juan: {porcentajeJuan:.2f}%")
print(f"Porcentaje de Rosa: {porcentajeRosa:.2f}%")
print(f"Porcentaje de Daniel: {porcentajeDaniel:.2f}%")