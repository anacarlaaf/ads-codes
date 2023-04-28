print("\nBem Vindo a Companhia de Logística da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)\n")  # identificador pessoal


def dimensoes_objeto():  # pergunta dimensões do objeto e retorna o multiplicador equivalente.

    while True:
        try:
            print("Dimensões (cm):")
            altura = float(input("Altura: "))
            comprimento: float = float(input("Comprimento: "))
            largura = float(input("Largura: "))
            volume = altura * comprimento * largura
            print("O volume do objeto é {} cm³.".format(volume))

            if volume < 1000:
                return 10
            if 1000 <= volume < 10000:
                return 20
            if 10000 <= volume < 30000:
                return 20
            if 30000 <= volume < 100000:
                return 20
            print("Não aceitamos objetos com volume maior que 100000 cm³. Por favor, tente novamente.\n")
            continue  # repetir o loop caso o volume for maior que o permitido.

        except ValueError:
            print("Valore inválido. Tente novamente.\n")
            continue  # repetir caso o usuário cometa um erro de digitação.


def peso_objeto():  # pergunta peso do objeto e retorna o multilpicador equivalente.

    while True:
        try:
            peso = float(input("\nPeso (kg): "))
            print("O peso do objeto é {} kg.".format(peso))

            if peso < 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                print("Não aceitamos objetos com peso maior que 30 kg. Por favor, tente novamente.")
                continue  # repetir o loop caso o peso for maior que o permitido.
            
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue  # repetir caso o usuário cometa um erro de digitação.


# dicionário com rotas como keys e multiplicadores como values.
rotas_m = {"RS": 1, "SR": 1, "BS": 1.2, "SB": 1.2, "BR": 1.5, "RB": 1.5}
rotas = ("\n_______________Rotas________________\n"
         "RS - De Rio de Janeiro até São Paulo\n"
         "SR - De São Paulo até Rio de Janeiro\n"
         "SR - De São Paulo até Rio de Janeiro\n"
         "SB - De São Paulo até Brasília\n"
         "BR - De Brasília até Rio de Janeiro\n"
         "RB - Rio de Janeiro até Brasília\n")


def rota_objeto():  # exibe rotas disponíveis, pergunta rota escolhida e retorna o multiplicador correspondente.
    print(rotas)

    while True:
        rota = input("Rota: ")

        if rota in rotas_m.keys():  # percorre o dicionário e retorna o multilpicador correspondente a rota escolhida.
            return rotas_m[rota]
        else:
            print("Rota inválida. Tente novamente.\n")
            continue  # repete o loop caso o valor digitado não corresponda a nenhuma key no dicionário.


# invoca funções
m_dimensoes = dimensoes_objeto()
m_peso = peso_objeto()
m_rota = rota_objeto()

total = m_dimensoes*m_peso*m_rota

print("\nDimensões: R${}\n"
      "Peso: R${}\n"
      "Rota: R${}".format(m_dimensoes, m_peso, m_rota))
print("Total a pagar (Dimensões x Peso x Rota): R${}".format(total))
