import os
os.system("cls")

añosAntiguedad = int(input("Ingresar años de antigüedad: "))
puntuacion = float(input("Ingresar puntuación del trabajador: "))

if añosAntiguedad > 2 and puntuacion > 90:
    bono = 200
else:
    bono = 100

print(f"Bono asignado: {bono}")