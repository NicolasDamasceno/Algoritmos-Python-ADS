from Q3 import juros_compostos
def main():
    valor_imovel = float(input('Valor do Imóvel(R$): '))
    entrada = float(input('Valor da Entrada(R$): '))
    juros_mensal = float(input('Juros Mensal(%): '))
    parcelas = int(input('Parcelas: '))

    valor_restante = valor_imovel - entrada
    print('---- Financiamento de Imóvel ----')
    print(f'Valor Total: R${valor_imovel}')
    print(f'Valor Financiado: R${valor_restante}\n')
    print(f'Valor das Parcerlas em x{parcelas}')
    for parcela in range(1,parcelas + 1, 1):
        if parcela == 1:
            valor_parcela = valor_restante / parcelas
            valor_parcela = juros_compostos(valor_parcela,juros_mensal,parcelas)
            valor_restante -= valor_parcela
            print(f'Parcela {parcela}: R${valor_parcela:0.2f}') 
        if parcela == 60:
            valor_parcela = valor_restante
            print(f'Parcela {parcela}: R${valor_parcela:0.2f}')  
            break
        else: 
            parcela_restante = parcelas - parcela
            valor_parcela = valor_restante / parcela_restante
            valor_parcela = juros_compostos(valor_parcela,juros_mensal, parcela_restante)
            valor_restante -= valor_parcela
            print(f'Parcela {parcela}: R${valor_parcela:0.2f}') 

if __name__ == '__main__':
    main()