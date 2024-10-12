import os, math
os.system("cls")

c1 = int(input("Longitud del primer cateto: "))
c2 = int(input("Longitud del segundo cateto: "))

h = math.sqrt (c1 ** 2 + c2 ** 2)

print(f"La hipotenusa del triángulo es: {h:.2f}")