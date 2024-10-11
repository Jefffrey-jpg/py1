import os, math
os.system("cls")

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

discriminante = b ** 2 - 4 * a * c

x1 = (-b + math.sqrt(discriminante)) / (2 * a) * (discriminante > 0) + (-b / (2 * a)) * (discriminante == 0)
x2 = (-b - math.sqrt(discriminante)) / (2 * a) * (discriminante > 0) + (-b / (2 * a)) * (discriminante == 0)
real = -b / (2 * a) * (discriminante < 0)
imaginario = math.sqrt(-discriminante) / (2 * a) * (discriminante < 0)

soluciones = f"Las soluciones son x1 = {x1} y x2 = {x2}" * (discriminante >= 0) + f"Las soluciones son x1 = {real} + {imaginario}i y x2 = {real} - {imaginario}i" * (discriminante < 0)

print(soluciones)