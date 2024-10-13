import os
os.system("cls")

sexo = input("Sexo del postulante (F para femenino, M para masculino): ").strip().upper()
edad = int(input("Edad del postulante: "))

if sexo == "F" :
    if edad < 23 :
        categoria = "FA"
    else :
        categoria = "FB"
elif sexo == "M" :
    if edad < 25 :
        categoria = "MA"
    else :
        categoria = "MB"
else :
    categoria = "Sexo no válido"

print(f"Categoría del postulante: {categoria}")
