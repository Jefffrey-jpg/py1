import os
os.system("cls")

numero = int(input("Ingrese un número de 4 cifras: "))

c1 = numero // 1000
c2 = (numero % 1000) // 100
c3 = (numero % 100) // 10
c4 = numero % 10

mayor = max(c1, c2, c3, c4)
menor = min(c1, c2, c3, c4)

if mayor > menor:
    numMayor = int(f"{mayor}{menor}")
else:
    numMayor = int(f"{menor}{mayor}")

print(f"El mayor número de dos cifras posible es: {numMayor}")