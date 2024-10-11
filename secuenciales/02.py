import os
os.system("cls")

m = float(input("Metros: "))

cm = m * 100.0
pulg = cm / 2.54
pie = pulg / 12
yard = pie / 3

print(f"Centímetros: {cm:.2f}")
print(f"Pulgadas: {pulg:.2f}")
print(f"Pies: {pie:.2f}")
print(f"Yardas: {yard:.2f}")