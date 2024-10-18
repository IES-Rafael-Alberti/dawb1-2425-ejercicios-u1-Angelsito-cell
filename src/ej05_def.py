def preciototal(res):
    return f"El precio final es de: {res}"

def main():
    imp = float(input("Precio SIN IVA:" ))
    iva = float(input("Introduzca el porcentaje de iva: " ))
    iva2= iva/100
    iva3 = imp*iva2
    res = imp+iva3
    print(preciototal(res))
    
if __name__ == "__main__":
    main()