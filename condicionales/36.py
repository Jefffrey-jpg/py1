import os
os.system("cls")

numCuadernos = int(input("Ingresar número de cuadernos adquiridos: "))

lapicerosLucas = 0
lapicerosFaber = 0
lapicerosPilot = 0

if numCuadernos < 12 :
    lapicerosLucas = 0
elif 12 <= numCuadernos < 24 :
    lapicerosLucas = numCuadernos // 4
elif 24 <= numCuadernos < 36 :
    lapicerosFaber = (numCuadernos // 4) * 2
elif numCuadernos >= 36 :
    lapicerosPilot = (numCuadernos // 4) * 2
    lapicerosFaber += numCuadernos // 6
    lapicerosLucas += numCuadernos // 12

print(f"Lapiceros Lucas: {lapicerosLucas}")
print(f"Lapiceros Faber: {lapicerosFaber}")
print(f"Lapiceros Pilot: {lapicerosPilot}")