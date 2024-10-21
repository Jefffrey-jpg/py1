import os, random, string
os.system("cls")

# Generador de contraseñas

def generarContraseña():
    longitud = int(input("Longitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {contraseña}")

generarContraseña()