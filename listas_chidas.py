def main():
    # numero = int(input("Dame un numero: "))
    # power = int(input("A cual potencia quieres elevarlos: ")) 
    
    # num_pow = []
    # # for num in range(1, numero + 1):
    # #     if num % 3 != 0:
    # #         num_pow.append(num ** power)


    # lista_corta = [ i ** 2 for i in range(1, numero + 1) if i % 3 != 0]

    lista_chida = [ i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]

    print(lista_chida)


if __name__ == '__main__':
    main()