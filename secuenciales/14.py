import os, math
os.system("cls")

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
num4 = int(input("Número 4: "))
num5 = int(input("Número 5: "))

numeros = [num1, num2, num3, num4, num5]

numeros.sort()
mayores = numeros[-3:]

promedio = sum(mayores) / 3

print(f"Promedio de los 3 mayores: {promedio:.2f}")