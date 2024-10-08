nombre = input("Dime el nombre del producto: ")
precio = float(input("Dame el precio del producto: "))
unidades = int(input("Dame el número de unidades que hay del producto: "))

preciofinal = precio/unidades

print(f'{nombre} cuesta {preciofinal:.2f}, tienes una cantidad de {unidades} unidades y todo cuesta {precio} euros')