
def pedir_numero():
    entrada = input("Introduzca un número: ")
    if entrada == "fin":
        return None
    try:
        numero = float(entrada)
        return numero
    except ValueError:
        print("Entrada inválida")
        return pedir_numero()

def calcular_estadisticas():
    total = 0
    contador = 0

    while True:
        numero = pedir_numero()
        if numero is None:
            break
        total += numero
        contador += 1

    if contador > 0:
        media = total / contador
    else:
        media = 0
    
    return total, contador, media

def main():
    total, contador, media = calcular_estadisticas()
    print(total, contador, media)

if __name__ == "__main__": 
    main()
