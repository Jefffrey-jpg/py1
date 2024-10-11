import os
os.system("cls")

monto = float(input("Ingrese el monto donado: S/. "))

montoSalud = monto * 0.25
montoComedor = monto * 0.35
montoEscuela = monto * 0.25
montoAsilo = monto * 0.15

print(f"Monto para el centro de salud: S/. {montoSalud:.2f}")
print(f"Monto para el comedor infantil: S/. {montoComedor:.2f}")
print(f"Monto para la escuela infantil: S/. {montoEscuela:.2f}")
print(f"Monto para el asilo de ancianos: S/. {montoAsilo:.2f}")