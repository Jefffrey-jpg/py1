import os
os.system("cls")

notas = []

nota1 = float(input("Calificación 1: "))
notas.append(nota1)

nota2 = float(input("Calificación 2: "))
notas.append(nota2)

nota3 = float(input("Calificación 3: "))
notas.append(nota3)

nota4 = float(input("Calificación 4: "))
notas.append(nota4)

nota5 = float(input("Calificación 5: "))
notas.append(nota5)

if len(notas) == 5:
    menor = min(notas)
    mayor = max(notas)
    
    notas.remove(menor)
    notas.remove(mayor)
    
    promedio = sum(notas) / len(notas)
    
    print(f"Notas eliminadas: {menor} y {mayor}")
    print(f"Promedio aprobatorio: {promedio:.2f}")