import os
os.system("cls")

donacion = float(input("Ingrese el monto de la donación: "))

if donacion >= 10000 :
    centroSalud = donacion * 0.30
    comedorNiños = donacion * 0.50
else :
    centroSalud = donacion * 0.25
    comedorNiños = donacion * 0.60

inversion = donacion - (centroSalud + comedorNiños)

print(f"Monto centro de salud: S/. {centroSalud:.2f}")
print(f"Monto comedor de niños: S/. {comedorNiños:.2f}")
print(f"Monto invertido: S/. {inversion:.2f}")