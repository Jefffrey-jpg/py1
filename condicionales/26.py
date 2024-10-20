import os
os.system("cls")

sueldoBasico = float(input("Ingresar sueldo básico: "))
añosAntiguedad = int(input("Ingresar años de antigüedad: "))
ventaTotal = float(input("Ingresar monto total de ventas: "))

if añosAntiguedad > 4 or ventaTotal > 5000:
    gratificacion = sueldoBasico * 0.25
else:
    gratificacion = sueldoBasico * 0.2

sueldoNeto = sueldoBasico + gratificacion

print("Gratificación:", gratificacion)
print("Sueldo neto:", sueldoNeto)