import os
os.system("cls")

unidades = int(input("Unidades: "))

compra = unidades * 20

if compra <= 500 : descuento = 0.12 * compra
elif compra <= 700: descuento = 0.14 * compra
else: descuento = 0.16 * compra

total = compra - descuento

if unidades <= 50 : caramelos = 5
elif unidades <= 100 : caramelos = 10
else: caramelos = 15

print(f("Compra: {compra}"))
print(f("Descuento: {descuento:.2f}"))
print(f("Total: {total:.2f}"))
print(f("Caramelos: {caramelos}"))