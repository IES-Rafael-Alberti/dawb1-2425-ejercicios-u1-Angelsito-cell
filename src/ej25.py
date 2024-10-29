nac = input("Cúando naciste? (DD/MM/YY): ")
componentes = nac.split('/')
if len(componentes) != 3:
    print("La fecha no es correcta. Asegúrate de usar dd/mm/aaaa.")
else:

    dia = componentes[0].zfill(2)
    mes = componentes[1].zfill(2)
    año = componentes[2]

    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {año}")