import os
os.system("cls")

unidadesA = int(input("Ingresar cantidad de unidades de producto A: "))
unidadesB = int(input("Ingresar cantidad de unidades de producto B: "))
precioA = 25
precioB = 30
importeBrutoA = unidadesA * precioA
importeBrutoB = unidadesB * precioB

if unidadesA > 50 :
    descuentoA = importeBrutoA * 0.15
else :
    descuentoA = 0

if unidadesB > 60 :
    descuentoB = importeBrutoB * 0.1
else :
    descuentoB = 0

importeBrutoTotal = importeBrutoA + importeBrutoB
descuentoTotal = descuentoA + descuentoB
totalPagar = importeBrutoTotal - descuentoTotal

print(f"Importe bruto total: {importeBrutoTotal}")
print(f"Descuento total: {descuentoTotal}")
print(f"Total a pagar: {totalPagar}")