from tabulate import tabulate

print("\nBem Vindo ao Controle de Estoque da Bicicletaria da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)")  # identificador pessoal

pecas = {}  # keys = código da peça, values = informações da peça


def cadastrar_peca(codigo):  # adiciona peça ao dict pecas

    while True:
        try:
            print("Casdastro de Peça")
            print("Código: ", codigo)
            nome = input("Nome: ")
            fabricante = input("Fabricante: ")
            valor = float(input("Valor: "))

            # adiciona as informações ao dicionário
            pecas[codigo] = [nome, fabricante, valor]
            print("Peça adicioanda com sucesso!")
            break

        except ValueError:  # retorna ao menu principal em caso de erro.
            print("Você digitou algum valor inválido. Tente novamente")
            continue


headers = ["Código", "Nome", "Fabricante", "Preço"]  # colunas da tabela de itens


def consultar_peca():  # pergunta forma de consulta e retorna item(ens)
    while True:
        try:
            print("\nConsultar Peças")
            print("\n1 - Consultar Tudo\n2 - Consultar por Código\n3 - Consultar por Fabricante\n4 - Voltar")
            print("___________________\n")
            resposta = int(input("Escolha a opção desejada: "))

            if resposta == 1:
                # tabela formatada com todos os itens
                print(tabulate([[k, ] + v for k, v in pecas.items()], headers=headers))

            if resposta == 2:
                codigo_consulta = int(input("Código: "))
                if codigo_consulta in pecas.keys():
                    # tabela formatada com ítens de códigos correspondentes
                    print(tabulate([[k, ] + v for k, v in pecas.items()
                                    if k == codigo_consulta], headers=headers))

                else:
                    print("Código não encontrado.")

            if resposta == 3:
                fabricante_consulta = input("Fabricante: ")
                # lista com todos os fabricantes
                fabricantes = [i[1] for i in pecas.values()]

                # verifica se fabricante digitado é válido
                if fabricante_consulta in fabricantes:
                    # tabela formatada com ítens de fabriantes correspondentes
                    print(tabulate([[k, ] + v for k, v in pecas.items()
                                    if v[1] == fabricante_consulta], headers=headers))

                else:  # retorna ao menu Consultar Peças
                    print("Fabricante não encontrado.")
                    continue

            if resposta == 4:  # retorna ao menu Consultar Peças
                break

        except ValueError:  # retorna ao menu principal em caso de erro.
            print("Opção inválida. Tente novamente.")
            continue


def remover_peca():  # pergunta o código da peça e a deleta do dictionário
    print("Remover Peça")
    codigo_remover = int(input("Código: "))

    if codigo_remover in pecas.keys():
        del pecas[codigo_remover]
        print("Peça removida com sucesso.")
    else:  # retorna ao menu principal caso haja erro
        print("Código não encontrado.")


def menu():  # menu principal

    while True:

        print("\n________MENU_______")
        print("\n1 - Cadastrar Peças\n2 - Consultar Peças\n3 - Remover Peças\n4 - Sair")
        print("___________________\n")

        try:
            resposta = int(input("Escolha a opção desejada: "))

            if resposta == 1:
                novo_codigo = len(pecas)+1  # cria um código para a nova peça
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


menu()  # inicia o programa
