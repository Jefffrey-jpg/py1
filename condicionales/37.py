import os
os.system("cls")

votosPamela = int(input("Ingresar votos para Pamela: "))
votosCarol = int(input("Ingresar votos para Carol: "))
votosFanny = int(input("Ingresar votos para Fanny: "))

totalVotos = votosPamela + votosCarol + votosFanny
mayoriaVotos = totalVotos / 2 + 1

ganador = ""

if votosPamela >= mayoriaVotos :
    ganador = "Pamela"
elif votosCarol >= mayoriaVotos :
    ganador = "Carol"
elif votosFanny >= mayoriaVotos :
    ganador = "Fanny"
else :
    if (votosPamela == votosCarol) or (votosPamela == votosFanny) or (votosCarol == votosFanny):
        ganador = "Empate"
    else:
        ganador = "Segunda vuelta"

print(f"Resultado de la elección: {ganador}")