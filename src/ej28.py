def leer_numero(mensaje):
    return int(input(mensaje))

def verificar_numeros_iguales(num1: int, num2: int):
     return num1 == num2

def calcular_numeros_entre(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    return len(range(num1 + 1, num2))

def mostrar_resultado(num1, num2):
    menor = min(num1, num2)
    mayor = max(num1, num2)
    cantidad = calcular_numeros_entre(num1, num2)
    print(f"El número menor es el {menor} y entre ellos existen {cantidad} números enteros.")

def main():
    num1 = leer_numero("Introduce un número: ")
    num2 = leer_numero("Introduce otro número: ")
    
    while verificar_numeros_iguales(num1, num2):
        print("**ERROR** Los números no pueden ser iguales. Por favor, introduce otro número.")
        num2 = leer_numero("Introduce otro número: ")
    mostrar_resultado(num1, num2)

if __name__ == "__main__":
    main()

    