def saludo(nombre):
    nombre = "Hola, " + nombre + "."
    return nombre

def main():

    nombre = input("Escribe tu nombre: ")
    print(saludo(nombre))

if __name__ == "__main__":
    main()