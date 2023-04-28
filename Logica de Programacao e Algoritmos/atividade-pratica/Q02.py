from tabulate import tabulate
import pandas as pd

print("\nBem Vindo a Lanchonete da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)\n")  # identificador pessoal

# dados do cardápio
codigos = list(range(100, 106)) + [200, 201]
precos = [9.00, 11.00, 12.00, 13.00, 14.00, 17.00, 5.00, 4.00]
itens = ["Cachorro-Quente", "Cachorro-Quente Duplo", "X-Egg", "X-Salada", "X-Bacon", "X-Tudo",
         "Refrigerante Lata", "Chá Gelado"]

data = list(zip(codigos, itens, precos))  # junção dos dados do cardápio em uma lista.
print("----------------- Cardápio -----------------")
print(tabulate(data, headers=["Código", "Descrição", "Valor(R$)"]))  # imprime tabela formatada com dados do cardápio.

cardapio = pd.DataFrame(data, columns=["codigos", "itens", "precos"])  # insere dados do cardápio em um DataFrame.


def calcular_total(codigo):  # recebe um código e retorna o item e o valor correspondentes.

    item = cardapio[cardapio["codigos"] == codigo]["itens"].item()
    preco = cardapio[cardapio["codigos"] == codigo]["precos"].item()
    print("Você adicionou ao pedido um {} no valor de R${}.\n".format(item, preco))
    return preco


def add_pedido():  # pergunta se o usuário deseja adicionar mais algum item ao pedido e retorna a resposta.
    while True:
        add_item = input("Deseja adicionar mais um item ao pedido? (S/N): ")

        if add_item in ("S", "N"):
            return add_item
        else:
            print("Resposta inválida. Tente novamente.\n")  # previne erros de digitação do usuário.
            continue


total = 0  # recebe o preço de cada item.

while True:  # loop para invocar as funções
    try:
        codigo_item = int(input("\nCódigo do pedido: "))
        total += calcular_total(codigo_item)
        resposta = add_pedido()

        if resposta == "S":
            continue  # repete o loop se a resposta do usuário for sim.
        else:
            break

    except (ValueError, ValueError):  # previne erros de digitação do usuário.
        print("Opção Inválida. Tente novamente.")
        continue

print("\n---------------------------------------------------")
print("\nTotal do pedido: R${}\nVolte sempre!".format(total))
