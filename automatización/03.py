import os, time
os.system("cls")

# Notas con tiempo (una especie de alarma)

def recordatorio():
    nota = input("Nota: ")
    tiempo = int(input("Tiempo en segundos para el recordatorio: "))
    print(f"El recordatorio aparecerá en {tiempo} segundos")
    time.sleep(tiempo)
    print(f"Es hora de: {nota}")

recordatorio()