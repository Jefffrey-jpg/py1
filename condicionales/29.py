import os
os.system("cls")

nota1 = float(input("Ingresar primera nota: "))
nota2 = float(input("Ingresar segunda nota: "))
nota3 = float(input("Ingresar tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio > 18:
    beca = 2000
elif promedio >= 15:
    beca = 1000
else:
    beca = 500

print(f"Promedio: {promedio}")
print(f"Beca asignada: {beca}")