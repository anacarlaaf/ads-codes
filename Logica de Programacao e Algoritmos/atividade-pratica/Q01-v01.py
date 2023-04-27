print("\nBem Vindo a Loja da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)\n")

while True:

    try:

        valor_produto = float(input("Valor da unidade do produto: "))
        quantidade_produto = int(input("Quantidade: "))

        if 10 < quantidade_produto <= 99:
            desconto = 0.05
            valor_desconto = valor_produto - valor_produto * desconto
            total = quantidade_produto*valor_desconto
            break

        elif 100 <= quantidade_produto <= 999:
            desconto = 0.10
            valor_desconto = valor_produto - valor_produto * desconto
            total = quantidade_produto * valor_desconto
            break

        elif quantidade_produto >= 1000:
            desconto = 0.15
            valor_desconto = valor_produto - valor_produto * desconto
            total = quantidade_produto * valor_desconto
            break

        else:
            desconto = 0
            total = quantidade_produto * valor_produto
            break

    except ValueError:
        print("Você deve digitar um número. Tente Novamente.\n")
        continue

print("\nValor Total: R$", valor_produto*quantidade_produto)
print("Valor com desconto: R${:.2f}   (desconto de {}%)".format(total, desconto*100))
