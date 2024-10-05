import os
os.system("cls")

def calcularPrecio(cantProd):
    if 1<= cantProd <=25 :
        precioUnidad=27
    elif 26<= cantProd <=50 :
        precioUnidad=25
    elif 51<= cantProd :
        precioUnidad=23
    else :
        return "Otro monto"

    importe = cantProd * precioUnidad
    descuento = 0.15 * importe if cantProd >50 else 0.5 * importe
    total = importe - descuento
    return round(importe, 2), round(descuento, 2), round(total, 2)

cantProd=int(input("Ingrese la cantidad del producto: "))
importe, descuento, total = calcularPrecio(cantProd)

print(f"Importe: S/. {importe}")
print(f"Descuento: S/. {descuento}")
print(f"Total: S/. {total}")
