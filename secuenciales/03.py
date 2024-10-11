import os
os.system("cls")

piesMetros = 1 / 3.2808
metrosYardas = 1 / 0.9144

tramo1=float(input("Primer tramo en kilometros: "))
tramo2=float(input("Segundo tramo en pies: "))
tramo3=float(input("Tercer tramo en millas: "))

tramo1Metros = tramo1 * 1000
tramo2Metros = tramo2 * piesMetros
tramo3Metros = tramo3 * 1609

distanciaTotalMetros = tramo1Metros + tramo2Metros + tramo3Metros
distanciaTotalYardas = distanciaTotalMetros * metrosYardas

print(f"Distancia total metros: {distanciaTotalMetros:.2f} metros.")
print(f"Distancia total yardas: {distanciaTotalYardas:.2f} yardas.")