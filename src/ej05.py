imp = int(input("Introduzca el importe sin IVA: "))
iva = int(input("Introduzca el tipo de IVA a aplicar: " "%"))

ivacompleto = iva/100 + 1

res = imp*ivacompleto

print("El precio con el IVA aplicado es: ", res,"euros")