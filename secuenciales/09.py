import os
os.system("cls")

numero = int(input("Ingrese un número de 4 cifras: "))

c1 = (numero // 1000) * (1000 <= numero <= 9999)
c2 = ((numero % 1000) // 100) * (1000 <= numero <= 9999)
c3 = ((numero % 100) // 10) * (1000 <= numero <= 9999)
c4 = (numero % 10) * (1000 <= numero <= 9999)

sumaCifras = c1 + c2 + c3 + c4

print(f"La suma de cifras es: {sumaCifras}")