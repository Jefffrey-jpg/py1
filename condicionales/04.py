import os
os.system("cls")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

if nota3 >= 10 :
    nota3 += 2
    if nota3 > 20 :
        nota3 = 20

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio final es: {promedio:.2f}")