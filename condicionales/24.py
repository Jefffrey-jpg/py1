import os
os.system("cls")

montoVendido = float(input("Ingresar monto total vendido: "))
sueldoBasico = 600
comision = montoVendido * 0.1

if montoVendido > 5000:
    bono = (montoVendido - 5000) // 500 * 25
else:
    bono = 0

sueldoTotal = sueldoBasico + comision + bono

print(f"Sueldo total del vendedor: {sueldoTotal}")