from tabulate import tabulate
import pandas as pd

print("\nBem Vindo a Lanchonete da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)\n")  # identificador pessoal

codigos = list(range(100, 106))+[200, 201]
precos = [9.00, 11.00, 12.00, 13.00, 14.00, 17.00, 5.00, 4.00]
itens = ["Cachorro-Quente", "Cachorro-Quente Duplo", "X-Egg", "X-Salada", "X-Bacon", "X-Tudo",
                   "Refrigerante Late", "Chá Gelado"]

data = list(zip(codigos, itens, precos))
print(tabulate(data, headers=["Código", "Descrição", "Valor(R$)"]))

cardapio = pd.DataFrame(data, columns=["codigos", "itens", "precos"])

total = 0


def calcular_total(codigo):  # verifica o preço e item correspondente ao código dado e retorna o total do pedido.
    item = cardapio[cardapio["codigos"] == codigo]["itens"].item()
    preco = cardapio[cardapio["codigos"] == codigo]["precos"].item()
    print("Você adicionou ao pedido um {} no valor de R${}.\n".format(item, preco))
    return total + preco

def perguntar_add_pedido(resposta):
    pass

while True:
    try:
        codigo_item = int(input("\nCódigo do pedido: "))
        total_pedido = calcular_total(codigo_item)


    except (ValueError, ValueError):
        print("Opção Inválida. Tente novamente.")
        continue
