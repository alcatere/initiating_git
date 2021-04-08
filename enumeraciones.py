

numero = int(input("Dame un entero"))
respuesta = 0

while respuesta**2 < numero:
    respuesta += 1

if respuesta**2 == numero:
    print(f'La raiz cuadrada de {numero} es {respuesta}')
else:
    print(f'El {numero} no tiene raiz cuadrada')