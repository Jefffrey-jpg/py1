import os
os.system("cls")

categoria = input("Ingresar categoría (A/B/C/D): ").strip().upper()
promedio = float(input("Ingresar promedio: "))
pension = 0
descuento = 0

if categoria == 'A' :
    pension = 550
    if promedio < 14 :
        descuento = 0
    elif 14 <= promedio < 16 :
        descuento = 0.10
    elif 16 <= promedio < 18 :
        descuento = 0.12
    else :
        descuento = 0.15
elif categoria == 'B' :
    pension = 500
    if promedio < 14 :
        descuento = 0
    elif 14 <= promedio < 16 :
        descuento = 0.10
    elif 16 <= promedio < 18 :
        descuento = 0.12
    else :
        descuento = 0.15
elif categoria == 'C' :
    pension = 450
    if promedio < 14 :
        descuento = 0
    elif 14 <= promedio < 16 :
        descuento = 0.10
    elif 16 <= promedio < 18 :
        descuento = 0.12
    else :
        descuento = 0.15
else :
    pension = 400
    if promedio < 14 :
        descuento = 0
    elif 14 <= promedio < 16 :
        descuento = 0.10
    elif 16 <= promedio < 18 :
        descuento = 0.12
    else :
        descuento = 0.15

nuevoPension = pension * (1 - descuento)

print(f"Pensión actual: {pension}")
print(f"Descuento: {pension * descuento}")
print(f"Nueva pensión: {nuevoPension}")
