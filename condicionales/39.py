import os
os.system("cls")

ausencia = float(input("Ingresar horas de ausencia: "))
tornillosDefectuosos = int(input("Ingresar cantidad de tornillos defectuosos: "))
tornillosNoDefectuosos = int(input("Ingresar cantidad de tornillos no defectuosos: "))

gradoEficiencia = 0
condicion1 = ausencia <= 1.5
condicion2 = tornillosDefectuosos < 300
condicion3 = tornillosNoDefectuosos > 10000

if condicion1 and condicion2 and condicion3 :
    gradoEficiencia = 20
elif condicion1 and condicion2 :
    gradoEficiencia = 12
elif condicion1 and condicion3 :
    gradoEficiencia = 13
elif condicion2 and condicion3 :
    gradoEficiencia = 15
elif condicion1 :
    gradoEficiencia = 7
elif condicion2 :
    gradoEficiencia = 8
elif condicion3 :
    gradoEficiencia = 9
else :
    gradoEficiencia = 5

print(f"Grado de eficiencia: {gradoEficiencia}")
