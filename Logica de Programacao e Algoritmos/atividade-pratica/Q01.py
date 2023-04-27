print("\nBem Vindo a Loja da Ana Carla!")
print("by Ana Carla de Araújo Fernandes (4346212)\n")  # identificador pessoal


def calcular_desconto(valor, quantidade):  # função para realização dos cálculos

    # estruturas de condição para definir qual desconto deve ser aplicado:
    if 10 < quantidade <= 99:
        desconto = 5

    elif 100 <= quantidade <= 999:
        desconto = 10

    elif quantidade >= 1000:
        desconto = 15

    else:
        desconto = 0

    valor_desconto = valor - valor * desconto / 100  # cálculo do valor com desconto
    total = quantidade * valor_desconto  # cálculo do valor sem desconto

    return "Valor Total: R$ {}, " \
           "\nValor com desconto: R${:.2f}   (desconto de {}%)".format(valor * quantidade, total, desconto)


valor_produto = 0  # receberá o valor da unidade do produto.
quantidade_produto = 0  # receberá quantas unidades serão adquiridas.

while True:  # Estrutura de repetição para lidar com erros de digitação do usuário.
    try:
        valor_produto = float(input("Valor da unidade do produto: "))
        quantidade_produto = int(input("Quantidade: "))
        break  # encerra o loop se o usuário digitar os valores corretamente.
    except ValueError:
        print("Você deve digitar um número. Tente Novamente.\n")
        continue  # reinicia o loop após erro de digitação.

# invoca função passando os parâmetros digitados pelo usuário e exibe o resultado.
print(calcular_desconto(valor_produto, quantidade_produto))
