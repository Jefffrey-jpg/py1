import os
os.system("cls")

codigo = int(input("Ingresar código de empleado (tres cifras): "))

tipoEmpleado = ""

if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0 :
    tipoEmpleado = "Administrativo"
elif codigo % 3 == 0 and codigo % 5 == 0 :
    tipoEmpleado = "Directivo"
elif codigo % 2 == 0 :
    tipoEmpleado = "Vendedor"
else :
    tipoEmpleado = "Seguridad"

print(f"Tipo de empleado: {tipoEmpleado}")