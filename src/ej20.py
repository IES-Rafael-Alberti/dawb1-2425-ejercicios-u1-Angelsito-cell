
num = input('Introduce tú número de teléfono (formato +34-número-extensión): ')
separar = num.split('-')
numfinal = separar[1]
print('El número de teléfono sin prefijo ni extensión es:', numfinal)