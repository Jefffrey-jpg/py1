import os
os.system("cls")

montoCompra = float(input("Ingresar monto total de la compra: "))

if montoCompra > 1000:
    descuento = montoCompra * 0.1
else:
    descuento = montoCompra * 0.05

pagoFinal = montoCompra - descuento

print(f"Descuento: {descuento}")
print(f"Pago final: {pagoFinal}")