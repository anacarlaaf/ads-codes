# talvez criar um dicionário mais organazado para os itens.

from tabulate import tabulate

print("\nBem Vindo ao Controle de Estoque da Bicicletaria da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)")  # identificador pessoal

pecas = {}  # receberá as informações dos itens


def cadastrar_peca(codigo):  # adiciona peça ao dict pecas
    print("Código: ", codigo)
    nome = input("Nome da peça: ")
    fabricante = input("Fabricante: ")
    valor = float(input("Valor (R$): "))

    pecas[codigo] = [nome, fabricante, valor]  # atribui as informações(values) no código(key)
    print("Peça adicionada com sucesso!")


headers = ["Código", "Produto", "Fabricante", "Preço"]  # títulos das colunas da tabela de consulta


def consultar_peca():  # pergunta forma de consulta e retorna item(ens)
    print("\n___CONSULTAR PEÇA___")
    print("\n1 - Consultar tudo\n2 - Consultar por Código\n3 - Consultar por Fabricante\n4 - Voltar")
    print("___________________")
    consulta = int(input("\nEscolha a opção desejada: "))

    while True:
        peca = []  # recebe as informações da peça consultada
        try:
            if consulta == 1:
                print("\n___________________PEÇAS__________________")
                # gera tebela formatada com todos os itens:
                return print(tabulate([[k, ] + v for k, v in pecas.items()], headers=headers))

            if consulta == 2:
                consulta_codigo = int(input("Código: "))
                peca.append(pecas[consulta_codigo])
                return print(tabulate(peca, headers=headers))  # printa

            if consulta == 2:
                consulta_fabricante = input("Fabricante: ")
                for value in pecas.values():
                    if consulta_fabricante == value:
                        peca.append(value)

            if consulta == 2:
                pass

        except IndexError:  # repete o loop caso o usuário cometa erro de digitação
            print("O banco de dados de peças está vazio. Adicione peças.")
            continue


def remover_peca():
    pass


def menu():

    while True:

        print("\n________MENU_______")
        print("\n1 - Cadastrar Peças\n2 - Consultar Peças\n3 - Remover Peças\n4 - Sair")
        print("___________________\n")

        try:
            resposta = int(input("Escolha a opção desejada: "))

            if resposta == 1:
                novo_codigo = len(pecas) + 1  # gera um novo código que será adicionado ao dict pecas
                cadastrar_peca(novo_codigo)
                continue

            if resposta == 2:
                consultar_peca()
                continue

            if resposta == 3:
                pass

            if resposta == 4:
                break  # encerra o programa

        except ValueError:  # repete o loop caso o usuário cometa um erro de digitação
            print("Opção Inválida. Tente novamente.\n")
            continue


menu()  # inicia programa
