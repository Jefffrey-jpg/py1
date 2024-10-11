import os
os.system("cls")

horas = float(input("Ingrese el número de horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: S/. "))

sueldoBasico = horas * tarifa

bonificacion = 0.2 * sueldoBasico
sueldoBruto = sueldoBasico + bonificacion

descuento = 0.1 * sueldoBruto
sueldoNeto = sueldoBruto - descuento

print(f"Sueldo básico: S/. {sueldoBasico:.2f}")
print(f"Sueldo bruto: S/. {sueldoBruto:.2f}")
print(f"Sueldo neto: S/. {sueldoNeto:.2f}")