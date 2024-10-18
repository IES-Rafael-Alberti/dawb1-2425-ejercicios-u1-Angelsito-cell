def leer_número(n):
     num =int(input(n))
     return num

def leer_incremento(mensaje2):
    incremento = int(input(mensaje2))
    return incremento

def leer_otronum(m):
     num2 =int(input(m))
     return num2

def verificar_inc(inc):
     return inc <= 0

def verficiar_num2(num2):
     return num2 <= 0 

def mostrar_resultado(serie, num, num2, inc):
    
     for i in range (num2): 
          cont = num + (i*inc)
          if i == 0:
               serie += str(cont) + "-"
          elif i == num2 -1: 
               serie += "-" + str(cont)
          elif i == 1: 
               serie += str(cont)
          else:
               serie += '..' + str(cont)

     print(f"SERIE => {serie}")

def main():
    num = leer_número("Introduce un num: ")
    inc = leer_incremento("Introduce el incremento: ")
    num2 = leer_otronum("Introduce el otro num: ")
    serie = ""

    while verificar_inc(inc):
         print("\n **Error** Incremento no puede ser 0 o menor a cero")
    int(input("Introduce el incremento: "))

    while verficiar_num2(num2):
         print("\n El segundo número no puede ser menor o igual a 0")
    int(input("Introduce el otro num: "))


    mostrar_resultado(serie, num, num2, inc)

if __name__ == "__main__":
    main()