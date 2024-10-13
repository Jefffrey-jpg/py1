import os
os.system("cls")

numero = int(input("Ingrese su número asignado: "))

eCivilCodigo = numero // 1000
edad = (numero // 10) % 100
sexoCodigo = numero % 10

if eCivilCodigo == 1 :
    eCivil = "Soltero"
elif eCivilCodigo == 2 :
    eCivil = "Casado"
elif eCivilCodigo == 3 :
    eCivil = "Divorciado"
elif eCivilCodigo == 4 :
    eCivil = "Viudo"
else :
    eCivil = "Codigo no válido"

if sexoCodigo == 1 :
    sexo = "Masculino"
elif sexoCodigo == 2 :
    sexo = "Femenino"
else :
    sexo = "Codigo no válido"

print(f"Estado civil: {eCivil}")
print(f"Edad: {edad}")
print(f"Sexo: {sexo}")