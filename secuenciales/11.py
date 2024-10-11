import os
os.system("cls")

num1 = int(input("Ingrese el primer numero de 3 cifras: "))
num2 = int(input("Ingrese el segundo numero de 3 cifras: "))

c1num1 = num1 // 100
c2num1 = (num1 // 10) % 10
c3num1 = num1 % 10

c1num2 = num2 // 100
c2num2 = (num2 // 10) % 10
c3num2 = num2 % 10

cambioNum1 = c3num2 * 100 + c2num1 * 10 + c1num2
cambioNum2 = c3num1 * 100 + c2num2 * 10 + c1num1

print(f"El nuevo primer número es: {cambioNum1}")
print(f"El nuevo segundo número es: {cambioNum2}")