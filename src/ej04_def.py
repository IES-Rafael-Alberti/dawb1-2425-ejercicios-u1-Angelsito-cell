def calculo(celsius, fahrenheit): 

    return f"{celsius} grados Celsius son {fahrenheit:.2f} grados fahrenheit"

def main(): 

    celsius = float(input("Introduce la temperatura en Grados Celsius: "))
    f = celsius*9/5 + 32
    print(calculo(celsius, f))

if __name__ == "__main__":
        main()
