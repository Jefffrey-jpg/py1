import os
os.system("cls")

puntajePorPuntualidad = int(input("Ingresar minutos de tardanza: "))
puntajePorRendimiento = int(input("Ingresar cantidad de observaciones: "))

if puntajePorPuntualidad == 0 :
    puntajePuntualidad = 10
elif 1 <= puntajePorPuntualidad <= 2 :
    puntajePuntualidad = 8
elif 3 <= puntajePorPuntualidad <= 5 :
    puntajePuntualidad = 6
elif 6 <= puntajePorPuntualidad <= 9 :
    puntajePuntualidad = 4
else :
    puntajePuntualidad = 0

if puntajePorRendimiento == 0 :
    puntajeRendimiento = 10
elif puntajePorRendimiento == 1 :
    puntajeRendimiento = 8
elif puntajePorRendimiento == 2 :
    puntajeRendimiento = 5
elif puntajePorRendimiento == 3 :
    puntajeRendimiento = 1
else :
    puntajeRendimiento = 0

puntajeTotal = puntajePuntualidad + puntajeRendimiento

if puntajeTotal < 11 :
    bonificacion = puntajeTotal * 2.5
elif 11 <= puntajeTotal <= 13 :
    bonificacion = puntajeTotal * 5.0
elif 14 <= puntajeTotal <= 16 :
    bonificacion = puntajeTotal * 7.5
elif 17 <= puntajeTotal <= 19 :
    bonificacion = puntajeTotal * 10.0
else :
    bonificacion = puntajeTotal * 12.5

print(f"Puntaje por puntualidad: {puntajePuntualidad}")
print(f"Puntaje por rendimiento: {puntajeRendimiento}")
print(f"Puntaje total: {puntajeTotal}")
print(f"Bonificación: {bonificacion}")