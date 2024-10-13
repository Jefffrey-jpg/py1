import os
os.system("cls")

sueldoBasico = 250
montoVendido = int(input("Ingrese el monto vendido: "))

if montoVendido < 5000 :
    comision = 0.05
elif montoVendido < 10000 :
    comision = 0.08
elif montoVendido < 20000 :
    comision = 0.10
elif montoVendido > 20000 :
    comision = 0.15
else :
    print("Cantidad de monto de venta no válido.")

sueldoBruto = sueldoBasico (montoVendido * comision)

if sueldoBruto > 3500 :
    descuento = 0.15
else:
    descuento = 0.08

montoDescuento = sueldoBruto * descuento
sueldoNeto = sueldoBruto - montoDescuento

print(f"Sueldo bruto: S/. {sueldoBruto:.2f}")
print(f"Comisión: S/. {(montoVendido * comision):.2f}")
print(f"Descuento: S/. {montoDescuento:.2f}")
print(f"Sueldo neto: S/. {sueldoNeto:.2f}")