peso = int(input("Introduzca su peso en kg: "))
altura= int(input("Introduzca su altura en centímetros: "))

alturareal= altura/100

imc= peso/alturareal**2
imc2= round(imc, 2)

print("Tu índice de masa corporal es: ",imc2)