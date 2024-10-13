import os
os.system("cls")

numeroTarjeta = int(input("Número de la tarjeta: "))
montoCompra = float(input("Monto de la compra: "))

if numeroTarjeta % 2 == 0 and numeroTarjeta >= 100:
    descuento = 0.15
else:
    descuento = 0.05

montoDescuento = montoCompra * descuento
montoFinal = montoCompra - montoDescuento

print(f"Número de la tarjeta: {numeroTarjeta}")
print(f"Monto de la compra: S/. {montoCompra:.2f}")
print(f"Descuento: {descuento * 100:.0f}%")
print(f"Monto final: S/. {montoFinal:.2f}")