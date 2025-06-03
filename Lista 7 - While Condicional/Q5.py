from in_onputs import obter_numero_real
# 5. Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
# sempre pelo mais barato.
def comparacao_precos(produto1, produto2, produto3):
    if produto1 < produto2 and produto1 < produto3:
        return produto1
    elif produto2 < produto1 and produto2 < produto3:
        return produto2
    elif produto3 < produto1 and produto3 < produto2:
        return produto3
    
def main():
    produto1 = obter_numero_real('Digite o preço do produto 1: ')
    produto2 = obter_numero_real('Digite o preço do produto 2: ')
    produto3 = obter_numero_real('Digite o preço do produto 3: ')

    print(f'A melhor compra é o produto de R${comparacao_precos(produto1,produto2,produto3)}')

if __name__ == '__main__':
    main()