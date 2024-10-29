def calculo(celsius): 
    f = celsius*9/5 + 32
    return "{:.2f} grados Celsius son {:.2f} grados fahrenheit".format(celsius, f)


def pruebaf(num: int) -> str:
    if num >= 0:
        num = num + 1
        num = num * num
        num = num / 2
    elif num <0: 
        return "El resultado no puede ser negativo"

    return f"El resultado es: {num}"


def hola(num):
    return str(num)

def main(): 

    celsius = float(input("Introduce la temperatura en Grados Celsius: "))
    celsius = round(celsius,2)
    print(calculo(celsius))

if __name__ == "__main__":
        main()