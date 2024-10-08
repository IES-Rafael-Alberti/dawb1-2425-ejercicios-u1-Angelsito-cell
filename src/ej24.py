precio = float(input("Introduzca el precio en euros: "))
rdondeo = round(precio,2)
precio2=str(rdondeo)

cents = rdondeo*100
cents2 = str(int(cents))

print(f"El precio dividido en Euros y cents es de {precio2} euros y {cents2} céntimos")
