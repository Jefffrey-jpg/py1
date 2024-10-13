import os
os.system("cls")

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

if a < b < c :
    orden = "ascendente"
elif a > b > c :
    orden = "descendente"
else :
    orden = "desorden"

print(f"Los números están en orden {orden}.")