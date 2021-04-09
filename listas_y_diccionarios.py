def main():
  lista1 = [1, "kha", True, 78]
  dict1 = {"firstname": "Rafael", "lastname": "Arana"}

  super_lista = [
    {"firstname": "Rafael", "lastname": "Arana"},
    {"firstname": "Maria", "lastname": "Romero"},
    {"firstname": "Francisco", "lastname": "Almaraz"},
    {"firstname": "Ana", "lastname": "Novelo"}
  ] 

  super_dict = {
    "numeros_nat": [1, 2, 3, 4],
    "numeros_neg": [-1, -2, -3, -4],
    "nombres": ["Rafa", "Maria", "Fernanda"]
  }
  print("Este es un Super Diccionario")
  for key, val in super_dict.items():
    print(f'{key} - {val}')

  print("\nEsta es una super lista")
  for dicc in super_lista:
    print(dicc)


if __name__ == '__main__':
  main()