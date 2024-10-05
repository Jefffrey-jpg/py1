cantProd=int(input("Cantidad del producto: "))

def calcularPrecio(cantProd)
    if 1<= cantProd <=25 :
        precioUnidad=27
    elif 26<= cantProd <=50 :
        precioUnidad=25
    elif 51<= cantProd :
        precioUnidad=23
    else :
        return "Ingrese otra cantidad"
