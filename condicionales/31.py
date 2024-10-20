import os
os.system("cls")

horasTrabajadas = float(input("Ingresar horas trabajadas: "))
categoria = input("Ingresar categoría (A/B/C/D): ").strip().upper()
tarifaPorHora = 0

if categoria == 'A':
    tarifaPorHora = 21.00
elif categoria == 'B':
    tarifaPorHora = 19.50
elif categoria == 'C':
    tarifaPorHora = 17.00
else:
    tarifaPorHora = 15.50

sueldoBruto = horasTrabajadas * tarifaPorHora
descuento = 0.20 if sueldoBruto > 2500 else 0.15

print(f"Sueldo bruto: {sueldoBruto}")
print(f"Descuento: {sueldoBruto * descuento}")
print(f"Sueldo neto: {sueldoBruto * (1 - descuento)}")