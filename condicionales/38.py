import os
os.system("cls")

mes = int(input("Ingresar mes (1-12): "))
anio = int(input("Ingresar año: "))
dias = 0

nombreMes = ""

if mes == 2 :
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) :
        dias = 29
    else :
        dias = 28
elif mes in [4, 6, 9, 11] : 
    dias = 30
else :
    dias = 31

nombreMes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"][mes - 1]

print(f"Días en el mes de {nombreMes}: {dias}")