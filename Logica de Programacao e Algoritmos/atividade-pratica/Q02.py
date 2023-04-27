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


while True:
    try:
        codigo = int(input("\nCódigo do pedido: "))
        item = cardapio[cardapio["codigos"] == codigo]["itens"].item()
        preco = cardapio[cardapio["codigos"] == codigo]["precos"].item()
        total += preco
        print("Você adicionou ao pedido um {} no valor de R${}.\n".format(item, preco))

        while True:
            add_item = input("Deseja adicionar mais um item ao pedido? (S/N): ")
            if add_item in ("S", "N"):
                break
            else:
                print("Resposta inválida. Tente novamente.")
                continue

        if add_item == "N":
            print("\nTotal a pagar: R${}.".format(total))
            break
        else:
            continue

    except (ValueError, ValueError):
        print("Opção Inválida. Tente novamente.")
        continue

