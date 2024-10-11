import os
os.system("cls")

cantidad = int(input("Ingrese la cantidad de unidades adquiridas: "))
precioUnidad = float(input("Ingrese el precio por unidad: S/. "))

importe = cantidad * precioUnidad

descuento1 = importe * 0.15
importeDescuento1 = importe - descuento1

descuento2 = importeDescuento1 * 0.15

descuentoTotal = descuento1 + descuento2

importeFinal = importe - descuentoTotal

print(f"Importe de la compra: S/. {importe:.2f}")
print(f"Descuento total: S/. {descuentoTotal:.2f}")
print(f"Importe a pagar: S/. {importeFinal:.2f}")