def main():
    number = int(input("Dame un numero: "))

    # dict1 = {}
    # for i in range(1,number + 1):
    #     if i % 4 != 0:
    #         dict1[i] = i ** 3

    dict_chida = {i: i ** 4 for i in range(1,number + 1) if i % 4 != 0}
    print(dict_chida)


if __name__ == '__main__':
    main()