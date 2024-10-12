import os
os.system("cls")

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

if (num1 > num2) and (num1 < num3) or (num1 < num2) and (num1 > num3):
    numeroMedio = num1
elif (num2 > num1) and (num2 < num3) or (num2 < num1) and (num2 > num3):
    numeroMedio = num2
else:
    numeroMedio = num3

print(f"Número intermedio: {numeroMedio}")