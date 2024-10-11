import os, math
os.system("cls")

print("Calcular área y volumen del cilindro")

h = int(input("Altura: "))
r = int(input("Radio: "))

areaLateral = 2 * math.pi * r * h
areaBases = 2 * math.pi * r ** 2
areaTotal = areaBases + areaLateral
vol = math.pi * h * r ** 2

print(f"El área del cilindro es: {areaTotal:.2f} m^2")
print(f"El volumen del cilindro es: {vol:.2f} m^3")