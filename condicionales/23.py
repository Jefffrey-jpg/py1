import os
os.system("cls")

notaMatematicas = float(input("Ingresar nota de Matemáticas: "))
notaFisica = float(input("Ingresar nota de Física: "))

if notaMatematicas > 17:
    propinaMatematicas = 3
else:
    propinaMatematicas = notaMatematicas

if notaFisica > 15:
    propinaFisica = 2
else:
    propinaFisica = 0.5

promedio = (notaMatematicas + notaFisica) / 2

if promedio > 16:
    obsequio = "Reloj"
else:
    obsequio = "Sin obsequio"

propinaTotal = propinaMatematicas + propinaFisica

print(f"Propina total: {propinaTotal}")
print(f"Obsequio: {obsequio}")