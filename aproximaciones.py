
numero = int(input("Introduce un numero: "))

epsilon = 0.01
paso = epsilon**2
respuesta = 0

while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
    respuesta += paso
if abs(respuesta**2 - numero) >= epsilon:
    print(f'No se encontro la raiz cuadrada del {numero}')
else:
    print(f'La raiz cuadrada de {numero} es {respuesta}')
    
