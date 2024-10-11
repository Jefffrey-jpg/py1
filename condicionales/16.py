import os
os.system("cls")

ingresoMensual = int(input("Ingreso mensual: S/. "))
costoCasa = int(input("Costo casa: S/. "))

if ingresoMensual <= 1250 :
    cuotaInicial = 0.15 * costoCasa
    cuotaMensual = (0.85 * costoCasa) / 120
else:
    cuotaInicial = 0.30 * costoCasa
    cuotaMensual = (0.70 * costoCasa) / 120

print(f"Cuota inicial: S/. {cuotaInicial:.2f}")
print(f"Cuota mensual: S/. {cuotaMensual:.2f}")