import os
os.system("cls")

numero = int(input("Ingrese un número de 4 cifras: "))

if 1000 <= numero <= 9999 :
    c1 = numero // 1000
    c2 = (numero % 1000) // 100
    c3 = (numero % 100) // 10
    c4 = numero % 10

    sumaCifras = c1 + c2 + c3 + c4

    print(f"La suma de cifras es: {sumaCifras}")
else:
    print(f"El numero ingresado no tiene 4 cifras")