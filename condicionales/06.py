import os
os.system("cls")

edad1 = int(input("Edad 1: "))
edad2 = int(input("Edad 2: "))
edad3 = int(input("Edad 3: "))

edadMayor = edad1
edadMenor = edad1

if edad2 > edadMayor:
    edadMayor = edad2
elif edad2 < edadMenor:
    edadMenor = edad2

if edad3 > edadMayor:
    edadMayor = edad3
elif edad3 < edadMenor:
    edadMenor = edad3

print(f"Edad mayor: {edadMayor}")
print(f"Edad menor: {edadMenor}")