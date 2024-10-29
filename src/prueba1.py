def mayor_numero(a, b):

    if a == b:
        return 0
    elif a > b:
         return a
    else:
        return b

def main():

    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))

    resultado = mayor_numero(a, b)

    if resultado == 0: 
        print("Los números son iguales")
    else: 
        print(f"El número mayor es: {resultado}" )

if __name__ == "__main__":
    main()