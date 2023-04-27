# fazer comentários

def calcular_desconto(valor, quantidade):
    if 10 < quantidade <= 99:
        desconto = 5

    elif 100 <= quantidade <= 999:
        desconto = 10

    elif quantidade >= 1000:
        desconto = 15

    else:
        desconto = 0

    valor_desconto = valor - valor * desconto/100
    total = quantidade * valor_desconto

    return "Valor Total: R$ {}, " \
           "\nValor com desconto: R${:.2f}   (desconto de {}%)".format(valor * quantidade, total, desconto)


valor_produto = 0
quantidade_produto = 0

while True:
    try:
        valor_produto = float(input("Valor da unidade do produto: "))
        quantidade_produto = int(input("Quantidade: "))
        break
    except ValueError:
        print("Você deve digitar um número. Tente Novamente.\n")
        continue

print(calcular_desconto(valor_produto, quantidade_produto))
