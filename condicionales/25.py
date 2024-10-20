import os
os.system("cls")

sueldoBruto = float(input("Ingresar sueldo bruto: "))
hijos = int(input("Ingresar número de hijos: "))

if hijos > 1 :
    bonificacion = sueldoBruto * 0.125 + hijos * 40
else :
    bonificacion = sueldoBruto * 0.1

sueldoNeto = sueldoBruto + bonificacion

print(f"Bonificación: {bonificacion}")
print(f"Sueldo neto: {sueldoNeto}")