import os
os.system("cls")

montoVendido = float(input("Ingresar el monto total vendido: S/. "))

comision = montoVendido * 0.09
sueldoBruto = comision + 500
descuento = sueldoBruto * 0.11
sueldoNeto = sueldoBruto - descuento

print(f"Comisión: S/. {comision:.2f}")
print(f"Sueldo Bruto: S/. {sueldoBruto:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo Neto: S/. {sueldoNeto:.2f}")