import os
os.system("cls")

notaPC1 = float(input("Ingresar nota de PC1: "))
notaPC2 = float(input("Ingresar nota de PC2: "))
notaPC3 = float(input("Ingresar nota de PC3: "))
notaEP = float(input("Ingresar nota de Examen Parcial: "))
notaEF = float(input("Ingresar nota de Examen Final: "))

promedio = (notaPC1 * 0.1) + (notaPC2 * 0.2) + (notaPC3 * 0.1) + (notaEP * 0.3) + (notaEF * 0.3)

condicion = "Aprobado" if promedio >= 13 else "Desaprobado"

print(f"Promedio final: {promedio}")
print(f"Condición: {condicion}")