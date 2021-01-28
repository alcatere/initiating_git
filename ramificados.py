numero1 = float(input( "Dame numero 1: "))
numero2 = float(input( "Dame numero 2: "))

if numero1 < numero2:
    print(f'El numero {numero1} es mas pequeño que {numero2}')
elif numero1 > numero2:
    print(f'El numero {numero1} es mas grande que {numero2}')
else:
    print( "Los numeros son iguales")