def calculo(celsius): 
    f = celsius*9/5 + 32
    return "{:.2f} grados Celsius son {:.2f} grados fahrenheit".format(celsius, f)

def main(): 

    celsius = float(input("Introduce la temperatura en Grados Celsius: "))
    celsius = round(celsius,2)
    print(calculo(celsius))

if __name__ == "__main__":
        main()