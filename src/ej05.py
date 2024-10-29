imp = int(input("Introduzca el importe sin IVA: "))
iva = int(input("Introduzca el tipo de IVA a aplicar: " "%"))

iva2= iva/100
iva3 = imp*iva2
res = imp+iva3

print("El precio con el IVA aplicado es: ", res,"euros")