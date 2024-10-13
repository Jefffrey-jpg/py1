import os
os.system("cls")

docenas = int(input("Docenas a comprar: "))
precioDocena = float(input("Precio por docena: "))

montoCompra = docenas * precioDocena

if docenas >= 6:
    descuento = 0.15
else:
    descuento = 0.10

montoDescuento = montoCompra * descuento
pagoTotal = montoCompra - montoDescuento

if docenas >= 30:
    lapiceros = (docenas // 3) * 2
else:
    lapiceros = 0

print(f"Monto de la compra: S/. {montoCompra:.2f}")
print(f"Descuento aplicado: S/. {montoDescuento:.2f}")
print(f"Pago total: S/. {pagoTotal:.2f}")
print(f"Lapiceros regalados: {lapiceros}")