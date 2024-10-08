def leer_nombre(mensaje):
     nombre =input(mensaje)
     return nombre

def leer_edad(mensaje2):
    edad = int(input(mensaje2))
    return edad

def verificar_nombre(nombre):
     return nombre 

def verificar_edad(edad):
     return edad <0 or edad > 125 

def mostrar_resultado(nombre, edad, falta):

    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {falta} años por cumplir")

def main():
    nombre = leer_nombre("Introduce tu nombre: ").strip()
    edad = leer_edad("Introduce tu edad: ")
    falta = 125 - edad

    if not nombre: 
            nombre = "{Desconocido}"

    while verificar_edad(edad):
         print("**ERROR** Introduce una edad entre 0 y 125 años")
         edad = leer_edad("Introduce tu edad: ")
    mostrar_resultado(nombre, edad, falta)

if __name__ == "__main__":
    main()