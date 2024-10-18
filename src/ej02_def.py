def horario(h, c):

    t = h*c
    return f"Importe total: {t} €"


def main():
    h = int(input("Introduzca las horas realizadas: "))
    c = int(input("Introduzca el coste por hora: "))
    
    print(horario(h, c))


if __name__ == "__main__":
    main()