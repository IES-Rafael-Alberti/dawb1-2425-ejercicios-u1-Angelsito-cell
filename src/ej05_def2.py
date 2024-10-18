def calcula_precio(imp: float, iva: float) -> str:
    iva = comprobar_iba(iva)

    iva = imp * iva
    importe = imp + iva
    return importe

def comprobar_iba(iva: float) -> str:
    if 0 < iva <= 1:
        return iva
    else:
        iva = 0.21
        iva = round(iva,2)
        return iva
    iva = round(iva,2)

def main():
    imp = float(input("Precio SIN IVA:" ))
    iva = float(input("Introduzca el porcentaje de iva: " ))
    
    importe = calcula_precio(imp, iva)

    ivacomp = comprobar_iba(iva)
    print(f"El precio final del artículo con IVA ({ivacomp}%) es {importe}€.")
    
if __name__ == "__main__":
    main()