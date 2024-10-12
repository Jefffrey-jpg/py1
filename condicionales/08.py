import os
os.system("cls")

propina = 20
propinaExamen = 5
examenesAprobados = int(input("Examenes aprovados: "))

if 0 <= examenesAprobados <= 3:
    propinaTotal = propina + (examenesAprobados * propinaExamen)
    print(f"La propina total es: S/. {propinaTotal}")