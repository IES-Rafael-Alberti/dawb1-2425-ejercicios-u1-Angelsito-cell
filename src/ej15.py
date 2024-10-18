cuenta = float(input("Introduce el dinero en la cuenta: "))

interés = 4/100

ahorro1 = round(cuenta*(1+interés),2)
ahorro2 = round(ahorro1*(1+interés),2)
ahorro3 = round(ahorro2*(1+interés),2)

print(f"La cantidad ahorrada en el primer año es de {ahorro1} euros")
print(f"La cantidad ahorrada en el segundo año es de {ahorro2} euros")
print(f"La cantidad ahorrada en el tercer año es de {ahorro3} euros")


