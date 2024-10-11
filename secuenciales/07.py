import os
os.system("cls")

b = int(input("Ingrese la base: "))
h = int(input("Ingrese la altura: "))

baseAltura = b + h
area = b * h
perimetro = baseAltura * 2

print(f"Área del rectángulo: {area} u^2.")
print(f"Perímetro del rectángulo: {perimetro} u.")