frase = input('Introduce una frase: ')
vocal = input('Introduce una vocal: ')

if vocal in ('a', 'e', 'i', 'o', 'u'):
    frase1 = frase.replace(vocal, vocal.upper())
    print(frase1)
else:
    print('La letra introducida no puede ser una distinta de una vocal')