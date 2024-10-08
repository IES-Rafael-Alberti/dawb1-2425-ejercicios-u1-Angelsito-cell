listacompra = input("Introduce la lista de la compra (separa los productos por comas): ")
lista = listacompra.split(",")

for producto in lista:
    print(producto.lstrip().rstrip())