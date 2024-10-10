import os
os.system("cls")

print("Calcular área y volumen del cilindro")

h = int(input("Altura: "))
r = int(input("Radio: "))

areaLateral = 2 * 3.14159264 * r * h
areaBases = 2 * 3.14159264 * r * r
areaTotal = areaBases + areaLateral
vol = 3.14159264 * r * r * h

print(f"El área del cilindro es: {areaTotal:.2f} m^2")
print(f"El volumen del cilindro es: {vol:.2f} m^3")