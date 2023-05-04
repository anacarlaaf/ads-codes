from tabulate import tabulate

print("\nBem Vindo ao Controle de Estoque da Bicicletaria da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)")  # identificador pessoal

pecas = {}  # receberá as informações dos itens


def cadastrar_peca(codigo):  # adiciona peça ao dict pecas

    while True:
        try:
            print("Casdastro de Peça")
            print("Código: ", codigo)
            nome = input("Nome: ")
            fabricante = input("Fabricante: ")
            valor = float(input("Valor: "))

            pecas[codigo] = [nome, fabricante, valor]
            print("Peça adicioanda com sucesso!")
            break

        except ValueError:
            print("Você digitou algum valor inválido. Tente novamente")
            continue


headers = ["Código", "Nome", "Fabricante", "Preço"]


def consultar_peca():  # pergunta forma de consulta e retorna item(ens)
    while True:
        try:
            print("\nConsultar Peça")
            print("\n1 - Consultar Tudo\n2 - Consultar por Código\n3 - Consultar por Fabricante\n4 - Voltar")
            print("___________________\n")
            resposta = int(input("Escolha a opção desejada: "))

            if resposta == 1:
                print(tabulate([[k, ] + v for k, v in pecas.items()], headers=headers))

            if resposta == 2:
                codigo_consulta = int(input("Código: "))
                if codigo_consulta in pecas.keys():
                    print(tabulate([[k, ] + v for k, v in pecas.items() if k == codigo_consulta], headers=headers))

                else:
                    print("Código não encontrado.")

            if resposta == 3:
                fabricante_consulta = input("Fabricante: ")
                fabricantes = [i[1] for i in pecas.values()]
                if fabricante_consulta in fabricantes:
                    print(tabulate([[k, ] + v for k, v in pecas.items() if v[1] == fabricante_consulta], headers=headers))

                else:
                    print("Fabricante não encontrado.")

            if resposta == 4:
                break

        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue


def remover_peca():
    print("Remover Peça")
    codigo_remover = int(input("Código: "))
    if codigo_remover in pecas.keys():
        del pecas[codigo_remover]
        print("Peça removida com sucesso.")
    else:
        print("Código não encontrado.")


def menu():

    while True:

        print("\n________MENU_______")
        print("\n1 - Cadastrar Peças\n2 - Consultar Peças\n3 - Remover Peças\n4 - Sair")
        print("___________________\n")

        try:
            resposta = int(input("Escolha a opção desejada: "))

            if resposta == 1:
                novo_codigo = len(pecas)+1
                cadastrar_peca(novo_codigo)
                continue

            if resposta == 2:
                consultar_peca()
                continue

            if resposta == 3:
                remover_peca()
                continue

            if resposta == 4:
                break  # encerra o programa

        except ValueError:  # repete o loop caso o usuário cometa um erro de digitação
            print("Opção Inválida. Tente novamente.\n")
            continue


menu()  # inicia programa
