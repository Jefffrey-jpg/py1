import os, math
os.system("cls")

r = int(input("Ingrese el radio del cilindro: "))
h = int(input("Ingrese la altura del cilindro: "))

areaBase = math.pi * r ** 2
areaLateral = 2 * math.pi * r * h
areaTotal= 2 * areaBase + areaLateral

print(f"Area de la base del cilindro: {areaBase:.2f} u^2")
print(f"Area lateral del cilindro: {areaLateral:.2f} u^2")
print(f"Area total del cilindro: {areaTotal:.2f} u^2")