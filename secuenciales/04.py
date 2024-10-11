import os
os.system("cls")

pies=int(input("Ingrese la cantidad de pies: "))
pulgadas=int(input("Ingrese la cantidad de pulgadas: "))

totalPulgadas = pies * 12 + pulgadas
metros = totalPulgadas * 0.0254

print(f"La estatura en metros es de: {metros:.2f} metros.")