import os
os.system("cls")

peso = float(input("Ingresar peso en kg: "))
estatura = float(input("Ingresar estatura en metros: "))

imc = peso / (estatura ** 2)

gradoObesidad = ""

if imc < 20 :
    gradoObesidad = "Delgado"
elif 20 <= imc <= 25 :
    gradoObesidad = "Normal"
elif 25 < imc <= 27 :
    gradoObesidad = "Sobrepeso"
else :
    gradoObesidad = "Obesidad"

print(f"IMC: {imc}")
print(f"Grado de obesidad: {gradoObesidad}")