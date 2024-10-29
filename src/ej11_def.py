
def resultado(num: int) -> str:
    if num >= 0:
        num = num + 1
        num = num * num
        num = num / 2
    elif num <0: 
        return "El resultado no puede ser negativo"

    return f"El resultado es: {num}"


def main():
    num = int(input('Introduzca un número: '))
    print(resultado(num))
    

if __name__ == "__main__":
    main()