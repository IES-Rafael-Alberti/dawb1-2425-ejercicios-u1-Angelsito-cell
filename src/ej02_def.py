def horario(total):
    return f"Importe total: {total} €"


def main():
    h = int(input("Introduzca las horas realizadas: "))
    c = int(input("Introduzca el coste por hora: "))
    t = h * c
    print(horario(h, c, t))


if __name__ == "__main__":
    main()