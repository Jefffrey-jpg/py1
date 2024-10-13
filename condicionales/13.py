import os
os.system("cls")

numero = int(input("Número de 3 cifras: "))

if 100 <= numero <= 999 :
    c1 = numero // 100
    c2 = (numero // 10) % 10
    c3 = numero % 10
    
    if (c1 + 1 == c2 and c2 + 1 == c3) or (c1 - 1 == c2 and c2 - 1 == c3) :
        print("Las cifras son consecutivas.")
    else :
        print("Las cifras no son consecutivas.")
else :
    print("El número no es de tres cifras.")