import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

discriminante = b ** 2 - 4 * a * c

if discriminante > 0 :
    x1 = (-b + math.sqrt (discriminante)) / (2 * a)
    x2 = (-b - math.sqrt (discriminante)) / (2 * a)
    print(f"Las soluciones son x1 = {x1} y x2 = {x2}")
elif discriminante == 0:
    x = -b / (2 * a)
    print(f"La solución es x = {x}")
else:
    real = -b / (2 * a)
    imaginario = math.sqrt (-discriminante) / (2 * a)
    print(f"Las soluciones son x1 = {real} + {imaginario}i y x2 = {real} - {imaginario}i")