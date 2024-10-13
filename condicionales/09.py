import os
os.system("cls")

producto = int(input("Ingrese el codigo del producto (101, 102, 103, 104): "))
unidades = int(input("Ingrese las unidades compradas: "))

if producto == 101 :
    precio = 17
elif producto == 102 :
    precio = 25
elif producto == 103 :
    precio = 16
elif producto == 104 :
    precio = 27
else :
    print("Código de producto no válido")

if 1 <= unidades <= 10 :
    descuento = 0.05
elif 11 <= unidades <= 20 :
    descuento = 0.08
elif 21 <= unidades <= 30 :
    descuento = 0.10
elif 31 <= unidades :
    descuento = 0.13
else :
    print("Descuento no aplicable")

importe = producto * unidades
montoDescuento = importe * descuento
precioFinal = importe - montoDescuento

print(f"Importe total: S/. {importe}")
print(f"Monto descontado: S/. {montoDescuento}")
print(f"Precio final: S/. {precioFinal}")