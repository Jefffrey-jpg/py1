import os
os.system("cls")

r = int(input("Ingrese el radio del cilindro: "))
h = int(input("Ingrese la altura del cilindro: "))

areaBase = 3.14159264 * r * r
areaLateral = 2 * 3.14159264 * r * h
areaTotal= 2 * areaBase + areaLateral

print(f"Area de la base del cilindro: {areaBase:.2f} u^2")
print(f"Area lateral del cilindro: {areaLateral:.2f} u^2")
print(f"Area total del cilindro: {areaTotal:.2f} u^2")